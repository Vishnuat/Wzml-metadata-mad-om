import os
import json
from asyncio import create_subprocess_exec
from asyncio.subprocess import PIPE
from bot import LOGGER, bot_cache


async def change_metadata(file, dirpath, key):
    LOGGER.info(f"Starting metadata modification for file: {file}")
    temp_file = f"{file}.temp.mkv"
    full_file_path = os.path.join(dirpath, file)
    temp_file_path = os.path.join(dirpath, temp_file)

    cmd = [
        "ffprobe",
        "-hide_banner",
        "-loglevel",
        "error",
        "-print_format",
        "json",
        "-show_streams",
        full_file_path,
    ]
    process = await create_subprocess_exec(*cmd, stdout=PIPE, stderr=PIPE)
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        LOGGER.error(f"Error getting stream info: {stderr.decode().strip()}")
        return file

    try:
        streams = json.loads(stdout)["streams"]
    except KeyError:
        LOGGER.error(
            f"No streams found in the ffprobe output: {stdout.decode().strip()}"
        )
        return file

    cmd = [
        bot_cache["pkgs"][2],
        "-y",
        "-i",
        full_file_path,
        "-c",
        "copy",
        "-metadata:s:v:0",
        f"title={key}",
        "-metadata",
        f"title={key}",
        "-metadata",
        f"copyright={key}",
        "-metadata",
        f"description={key}",
        "-metadata",
        f"license={key}",
        "-metadata",
        f"LICENSE={key}",
        "-metadata",
        f"author={key}",
        "-metadata",
        f"summary={key}",
        "-metadata",
        f"comment={key}",
        "-metadata",
        f"artist={key}",
        "-metadata",
        f"album={key}",
        "-metadata",
        f"genre={key}",
        "-metadata",
        f"date={key}",
        "-metadata",
        f"creation_time={key}",
        "-metadata",
        f"language={key}",
        "-metadata",
        f"publisher={key}",
        "-metadata",
        f"encoder={key}",
        "-metadata",
        f"SUMMARY={key}",
        "-metadata",
        f"AUTHOR={key}",
        "-metadata",
        f"WEBSITE={key}",
        "-metadata",
        f"COMMENT={key}",
        "-metadata",
        f"ENCODER={key}",
        "-metadata",
        f"FILENAME={key}",
        "-metadata",
        f"MIMETYPE={key}",
        "-metadata",
        f"PURL={key}",
        "-metadata",
        f"ALBUM={key}",
    ]

    audio_index = 0
    subtitle_index = 0
    first_video = False

    for stream in streams:
        stream_index = stream["index"]
        stream_type = stream["codec_type"]

        if stream_type == "video":
            if not first_video:
                cmd.extend(["-map", f"0:{stream_index}"])
                first_video = True
            cmd.extend([f"-metadata:s:v:{stream_index}", f"title={key}"])
        elif stream_type == "audio":
            cmd.extend(
                [
                    "-map",
                    f"0:{stream_index}",
                    f"-metadata:s:a:{audio_index}",
                    f"title={key}",
                ]
            )
            audio_index += 1
        elif stream_type == "subtitle":
            codec_name = stream.get("codec_name", "unknown")
            if codec_name in ["webvtt", "unknown"]:
                LOGGER.warning(
                    f"Skipping unsupported subtitle metadata modification: {codec_name} for stream {stream_index}"
                )
            else:
                cmd.extend(
                    [
                        "-map",
                        f"0:{stream_index}",
                        f"-metadata:s:s:{subtitle_index}",
                        f"title={key}",
                    ]
                )
                subtitle_index += 1
        else:
            cmd.extend(["-map", f"0:{stream_index}"])

    cmd.append(temp_file_path)

    process = await create_subprocess_exec(*cmd, stderr=PIPE, stdout=PIPE)
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        err = stderr.decode().strip()
        LOGGER.error(err)
        LOGGER.error(f"Error modifying metadata for file: {file}")
        return file

    os.replace(temp_file_path, full_file_path)
    LOGGER.info(f"Metadata modified successfully for file: {file}")
    return file


async def add_attachment(file, dirpath, attachment_path):
    LOGGER.info(f"Adding photo attachment to file: {file}")

    temp_file = f"{file}.temp.mkv"
    full_file_path = os.path.join(dirpath, file)
    temp_file_path = os.path.join(dirpath, temp_file)

    attachment_ext = attachment_path.split(".")[-1].lower()
    if attachment_ext in ["jpg", "jpeg"]:
        mime_type = "image/jpeg"
    elif attachment_ext == "png":
        mime_type = "image/png"
    else:
        mime_type = "application/octet-stream"

    cmd = [
        "xtra",
        "-y",
        "-i",
        full_file_path,
        "-attach",
        attachment_path,
        "-metadata:s:t",
        f"mimetype={mime_type}",
        "-c",
        "copy",
        "-map",
        "0",
        temp_file_path,
    ]

    process = await create_subprocess_exec(*cmd, stderr=PIPE, stdout=PIPE)
    stdout, stderr = await process.communicate()

    if process.returncode != 0:
        err = stderr.decode().strip()
        LOGGER.error(err)
        LOGGER.error(f"Error adding photo attachment to file: {file}")
        return file

    os.replace(temp_file_path, full_file_path)
    LOGGER.info(f"Photo attachment added successfully to file: {file}")
    return file

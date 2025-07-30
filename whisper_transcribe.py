import whisper
import os
from pydub import AudioSegment
from whisper.utils import get_writer
import json

# Load the Whisper model
model = whisper.load_model("base.en") # Or your preferred model size

input_root_directory = './input_audio'
output_base_directory = "./transcriptions"

if not os.path.exists(output_base_directory):
    os.makedirs(output_base_directory)

supported_extensions = ('.opus', '.aac', '.ogg', '.mp3', '.wav', '.m4a')

# Define the output formats you want
# output_formats = ["txt", "segmented_txt", "srt", "vtt", "json"]
output_formats = ["txt", "segmented_txt", "vtt"]

initial_prompt_text = "This is a recording in British English, focusing on everyday conversations. Aluminium, recognise, organise, litre, analyse, favourite, centre, colour, theatre, apologise, realise, licence, defence."

# --- Helper function to format time for the segmented_txt output ---
def format_whisper_cli_timestamp(seconds):
    """Formats a float of seconds into [MM:SS.mmm] format as seen in Whisper CLI."""
    minutes = int(seconds // 60)
    seconds_remainder = seconds % 60
    return f"{minutes:02d}:{seconds_remainder:06.3f}"


# --- Main processing loop using os.walk() ---
for root, _, files in os.walk(input_root_directory):
    # 'root' is the current directory being walked
    # '_' (dirnames) is a list of subdirectories in 'root' (we don't need it here)
    # 'files' is a list of filenames in 'root'

    # Determine the corresponding output directory for the current 'root'
    # This maintains the directory structure in the output folder
    relative_path = os.path.relpath(root, input_root_directory)
    current_output_directory = os.path.join(output_base_directory, relative_path)

    if not os.path.exists(current_output_directory):
        os.makedirs(current_output_directory)

    for filename in files:
        if filename.lower().endswith(supported_extensions):
            input_filepath = os.path.join(root, filename)
            base_filename = os.path.splitext(filename)[0]

            print(f"Processing: {input_filepath}") # Print full path for clarity

            audio_to_transcribe = input_filepath

            try:
                result = model.transcribe(
                    audio_to_transcribe,
                    language="en",
                    initial_prompt=initial_prompt_text
                )

                # --- Save outputs in all desired formats ---
                for fmt in output_formats:
                    # Output files will be saved in the corresponding subdirectory
                    output_filepath_base = os.path.join(current_output_directory, base_filename)

                    if fmt == "txt":
                        with open(f"{output_filepath_base}.txt", "w", encoding="utf-8") as f:
                            f.write(result["text"].strip())
                        print(f"  Saved {filename} as .txt (continuous)")

                    elif fmt == "segmented_txt":
                        output_file = f"{output_filepath_base}_segmented.txt"
                        with open(output_file, "w", encoding="utf-8") as f:
                            for segment in result["segments"]:
                                start_time = format_whisper_cli_timestamp(segment["start"])
                                end_time = format_whisper_cli_timestamp(segment["end"])
                                text = segment["text"].strip()
                                f.write(f"[{start_time} --> {end_time}] {text}\n")
                        print(f"  Saved {filename} as .txt (segmented CLI-like)")

                    elif fmt == "json":
                        with open(f"{output_filepath_base}.json", "w", encoding="utf-8") as f:
                            json.dump(result, f, ensure_ascii=False, indent=4)
                        print(f"  Saved {filename} as .json")

                    else:
                        writer = get_writer(fmt, current_output_directory) # Ensure writer uses current_output_directory
                        writer(result, output_filepath_base)
                        print(f"  Saved {filename} as .{fmt}")

            except Exception as e:
                print(f"Error processing {input_filepath}: {e}")

print("\nAll transcriptions complete for all specified formats.")
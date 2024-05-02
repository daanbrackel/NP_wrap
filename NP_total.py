import os
import argparse
import pandas as pd

def extract_barcode(folder_name):
    # Extract the barcode number from the folder name
    return folder_name.split('_')[-1].split('.')[0]

def run_nanoplot(input_directory, output_directory):
    # Loop through each FASTQ file in the input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.fastq.gz'):
            input_filepath = os.path.join(input_directory, filename)
            output_folder = os.path.splitext(filename)[0]  # Use file name without extension as output folder name
            output_folder_path = os.path.join(output_directory, output_folder)
            os.makedirs(output_folder_path, exist_ok=True)
            
            # Run NanoPlot on the current file
            command = f'NanoPlot --fastq {input_filepath} --tsv_stats --outdir {output_folder_path}'
            os.system(command)

def merge_nanostats(input_directory, output_directory):
    data = {}  # Dictionary to hold the data for each barcode
    
    # Iterate over each folder in the input directory
    for folder_name in os.listdir(input_directory):
        folder_path = os.path.join(input_directory, folder_name)
        if os.path.isdir(folder_path):
            barcode = extract_barcode(folder_name)
            nanostats_file = os.path.join(folder_path, 'NanoStats.txt')
            if os.path.exists(nanostats_file):
                # Read NanoStats.txt into a DataFrame
                barcode_data = pd.read_csv(nanostats_file, sep='\t', index_col=0, header=None, names=[barcode])
                # Store the relevant data into the dictionary
                data[barcode] = barcode_data.loc[:, barcode]

    # Create a DataFrame from the dictionary, sorted by barcode
    merged_data = pd.DataFrame(data)
    merged_data = merged_data.reindex(sorted(merged_data.columns), axis=1)
    
    # Write the merged data to a TSV file in the same directory as the output directory
    output_file = os.path.join(output_directory, 'DataFrame.tsv')
    merged_data.to_csv(output_file, sep='\t', index_label='Metrics')

def main():
    # Argument parser setup
    parser = argparse.ArgumentParser(description='Run NanoPlot on multiple FASTQ files and merge NanoStats from multiple barcode folders into one TSV file.')
    parser.add_argument('input_directory', type=str, help='Input directory containing FASTQ files.')
    parser.add_argument('output_directory', type=str, help='Output directory for NanoPlot results.')
    args = parser.parse_args()

    # Run NanoPlot
    run_nanoplot(args.input_directory, args.output_directory)

    # Merge NanoStats
    merge_nanostats(args.output_directory, args.output_directory)

if __name__ == "__main__":
    main()

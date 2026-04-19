# ECE105 Lab 3 Sensor Plots

A Python script that generates publication-quality visualizations of synthetic temperature sensor data using NumPy and Matplotlib.

## Installation

1. Activate the `ece105` conda environment:
   ```
   conda activate ece105
   ```

2. Install the required dependencies using conda or mamba:
   ```
   conda install numpy matplotlib
   ```
   or
   ```
   mamba install numpy matplotlib
   ```

## Usage

Run the script from the command line:
```
python generate_plots.py
```

## Example Output

The script produces a single PNG file named `sensor_analysis.png` containing three side-by-side plots:

1. **Scatter Plot**: Shows temperature readings from Sensor A (blue) and Sensor B (orange) plotted against time, illustrating the temporal distribution of measurements.

2. **Histogram**: Displays the temperature distribution for both sensors as overlaid histograms with vertical lines indicating the mean temperature for each sensor.

3. **Box Plot**: Presents a side-by-side comparison of the temperature distributions using box plots, with a horizontal line showing the overall mean temperature across both sensors.

## AI Tools Used and Disclosure

[Placeholder: Describe any AI tools used in the development of this project, including how they were utilized and any relevant disclosures.]



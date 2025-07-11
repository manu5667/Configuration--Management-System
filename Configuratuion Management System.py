import configparser
import json
import os
from datetime import datetime

class ConfigurationManager:
    def __init__(self, config_file_path):
        self.config_file_path = config_file_path
        self.config_data = {}
        
    def read_config(self):
        """Read and parse the configuration file."""
        try:
            if not os.path.exists(self.config_file_path):
                raise FileNotFoundError(f"Configuration file not found: {self.config_file_path}")
            
            config = configparser.ConfigParser()
            config.read(self.config_file_path)
            
            # Extract data from each section
            for section in config.sections():
                self.config_data[section] = dict(config[section])
            
            return True
            
        except configparser.Error as e:
            print(f"Error parsing configuration file: {str(e)}")
            return False
        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            return False
    
    def save_to_json(self, output_file='config_output.json'):
        """Save the configuration data to a JSON file."""
        try:
            # Add timestamp to the data
            output_data = {
                'timestamp': datetime.utcnow().isoformat(),
                'config': self.config_data
            }
            
            # Save to JSON file
            with open(output_file, 'w') as f:
                json.dump(output_data, f, indent=4)
            
            return True
        except Exception as e:
            print(f"Error saving to JSON file: {str(e)}")
            return False
    
    def get_config_data(self):
        """Return the parsed configuration data."""
        return self.config_data

def get_file_path():
    """Get file path and validate it."""
    while True:
        file_path = input("Please enter the full path to your config file (e.g., C:\\Users\\YourName\\config.ini): ").strip()
        
        # Remove quotes if the user included them
        file_path = file_path.strip('"\'')
        
        # Check if the file exists
        if os.path.exists(file_path):
            return file_path
        else:
            print(f"Error: File not found at '{file_path}'")
            retry = input("Would you like to try again? (yes/no): ").lower()
            if retry != 'yes':
                return None

def get_output_path():
    """Get output file path and validate it."""
    while True:
        output_path = input("Please enter the full path for the output JSON file (e.g., C:\\Users\\YourName\\output.json): ").strip()
        
        # Remove quotes if the user included them
        output_path = output_path.strip('"\'')
        
        try:
            # Check if the directory exists
            output_dir = os.path.dirname(output_path)
            if output_dir and not os.path.exists(output_dir):
                print(f"Directory '{output_dir}' does not exist.")
                create_dir = input("Would you like to create this directory? (yes/no): ").lower()
                if create_dir == 'yes':
                    os.makedirs(output_dir)
                else:
                    continue
            
            # Test if we can write to this location
            if output_dir:
                if not os.access(output_dir, os.W_OK):
                    print(f"Error: No write permission for directory '{output_dir}'")
                    continue
            
            return output_path
            
        except Exception as e:
            print(f"Error: {str(e)}")
            retry = input("Would you like to try again? (yes/no): ").lower()
            if retry != 'yes':
                return None

def main():
    print("Configuration File Parser")
    print("=" * 25)
    
    # Get input file path
    input_path = get_file_path()
    if not input_path:
        print("Program terminated: No valid input file provided.")
        return
    
    # Get output file path
    output_path = get_output_path()
    if not output_path:
        print("Program terminated: No valid output location provided.")
        return
    
    # Initialize configuration manager
    config_manager = ConfigurationManager(input_path)
    
    # Read and parse configuration
    if config_manager.read_config():
        print("\nConfiguration File Parser Results:")
        for section, values in config_manager.get_config_data().items():
            print(f"\n{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
        
        # Save to JSON file
        if config_manager.save_to_json(output_path):
            print(f"\nConfiguration successfully saved to: {output_path}")
        else:
            print("\nError saving configuration to JSON file")
    else:
        print("Failed to read configuration file")

if __name__ == '__main__':
    main()

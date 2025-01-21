from typing import List, Dict, Any
import pandas as pd
from datetime import datetime
import json

class SmartDataProcessor:
    """
    A flexible data processing pipeline that can handle multiple data formats
    and perform intelligent transformations.
    """
    
    def __init__(self):
        self.transformations = []
        
    def add_transformation(self, func):
        """Add a transformation to the pipeline."""
        self.transformations.append(func)
        return self
        
    def process(self, data: Any) -> Dict:
        """Process the input data through all transformations."""
        # First, convert input to standard format
        processed_data = self._standardize_input(data)
        
        # Apply all transformations
        for transform in self.transformations:
            processed_data = transform(processed_data)
            
        return processed_data
    
    def _standardize_input(self, data: Any) -> Dict:
        """Convert various input formats to standard dictionary format."""
        if isinstance(data, str):
            try:
                return json.loads(data)
            except json.JSONDecodeError:
                # Try parsing as CSV
                return pd.read_csv(StringIO(data)).to_dict(orient='records')[0]
        elif isinstance(data, pd.DataFrame):
            return data.to_dict(orient='records')[0]
        elif isinstance(data, dict):
            return data
        else:
            raise ValueError(f"Unsupported input type: {type(data)}")

# Example transformations
def clean_dates(data: Dict) -> Dict:
    """Convert string dates to datetime objects."""
    for key, value in data.items():
        if isinstance(value, str):
            try:
                data[key] = datetime.strptime(value, "%Y-%m-%d")
            except ValueError:
                pass
    return data

def calculate_metrics(data: Dict) -> Dict:
    """Add derived metrics based on existing data."""
    if 'revenue' in data and 'costs' in data:
        data['profit'] = data['revenue'] - data['costs']
        data['margin'] = (data['profit'] / data['revenue']) * 100 if data['revenue'] else 0
    return data

# Usage example
if __name__ == "__main__":
    # Create processor with transformations
    processor = SmartDataProcessor()
    processor.add_transformation(clean_dates)
    processor.add_transformation(calculate_metrics)
    
    # Example input data
    sample_data = {
        "date": "2024-01-15",
        "revenue": 1000,
        "costs": 600,
        "customer_id": "C123"
    }
    
    # Process the data
    result = processor.process(sample_data)
    print(json.dumps(result, default=str, indent=2))
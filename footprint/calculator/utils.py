
# helper function to calculate emission
import pandas as pd
from .models import OfficeOperationForm, EmissionFactor


class EmissionCalculator:
    @staticmethod
    def calculate_emission():
        # Fetch data from the models
        office_operation_data = OfficeOperationForm.objects.values()
        emission_factor_data = EmissionFactor.objects.values()

        # Convert the QuerySet to DataFrame
        office_operation_df = pd.DataFrame.from_records(office_operation_data)
        emission_factor_df = pd.DataFrame.from_records(emission_factor_data)

        # Remove non-matching columns
        office_operation = office_operation_df.drop(columns=['id', 'year'])
        emission_factor_df = emission_factor_df.drop(columns=['id'])

        # Rename columns in emission_factor_df to match office_operation_df for multiplication
        emission_factor_df.columns = office_operation.columns

        # Multiply the dataframes
        result_df = office_operation * emission_factor_df.iloc[0]

        # Add a column for total emission
        result_df['Total Emission'] = result_df.sum(axis=1)

        # Add the 'year' column from office_operation_df to result_df as the first column
        result_df.insert(0, 'year', office_operation_df['year'])

        return result_df
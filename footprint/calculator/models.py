from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime

PERCENTAGE_VALIDATOR = [MinValueValidator(0), MaxValueValidator(100)]

# Create your models here.

class OfficeOperationForm(models.Model):
	year = models.IntegerField(validators=[MinValueValidator(2000), MaxValueValidator(9999)], default=datetime.now().year)
	electricity = models.IntegerField(default=1000)
	water = models.IntegerField(default=1000)
	paper = models.IntegerField(default=50)
	garbage = models.IntegerField(default=1)
	food = models.DecimalField(max_digits=3, decimal_places=0, default=0, validators=PERCENTAGE_VALIDATOR)
	commute = models.IntegerField(default=1500)

	class Meta:
		app_label = 'calculator'


class EmissionFactor(models.Model):
	ef_electricity = models.DecimalField(max_digits=5, decimal_places=3)
	ef_water = models.DecimalField(max_digits=5, decimal_places=3)
	ef_paper = models.DecimalField(max_digits=5, decimal_places=3)
	ef_garbage = models.DecimalField(max_digits=5, decimal_places=3)
	ef_food = models.DecimalField(max_digits=5, decimal_places=3)
	ef_commute = models.DecimalField(max_digits=5, decimal_places=3)


# def calculate_emission():
#     # Fetch data from the models
#     office_operation_data = OfficeOperationForm.objects.values()
#     emission_factor_data = EmissionFactor.objects.values()

#     # Convert the QuerySet to DataFrame
#     office_operation_df = pd.DataFrame.from_records(office_operation_data)
#     emission_factor_df = pd.DataFrame.from_records(emission_factor_data)

#     # Remove non-matching columns
#     office_operation_df = office_operation_df.drop(columns=['id', 'year'])
#     emission_factor_df = emission_factor_df.drop(columns=['id'])

#     # Rename columns in emission_factor_df to match office_operation_df for multiplication
#     emission_factor_df.columns = office_operation_df.columns

#     # Multiply the dataframes
#     result_df = office_operation_df * emission_factor_df

#     print(result_df)
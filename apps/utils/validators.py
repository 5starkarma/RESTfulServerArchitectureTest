from datetime import datetime

from rest_framework import serializers


class VehicleYearValidator(object):

    def __call__(self, year, *args, **kwargs):
        """
        Validates the year of the boat is >1800 or this year +1 due
        to some models being released a year early.
        :return:

        """
        current_year = datetime.now().year
        if not (1800 < year <= (current_year + 1)):
            raise serializers.ValidationError(f"The year must be between 1800-{(current_year + 1)}")
        return year

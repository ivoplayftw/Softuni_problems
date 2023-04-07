from calendar import month_name


class Dvd:
    def __init__(self, creation_year, name, id_num, creation_month, age_restriction):
        self.name = name
        self.creation_year = creation_year
        self.id = id_num
        self.creation_month = creation_month
        self.age_restriction = age_restriction
        self.is_rented = False

    @classmethod
    def from_date(cls, name, date, age_restriction):
        day, month, year = [int(x) for x in date.split(".")]
        return cls(name, id, year, month_name[month], age_restriction)

    def __repr__(self):
        return f"{self.id}: {self.name} ({self.creation_month} {self.creation_year})" \
               f" has age restriction {self.age_restriction}." \
               f" Status: {'rented' if self.is_rented else 'not rented'}"

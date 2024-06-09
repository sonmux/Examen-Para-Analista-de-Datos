# Customer
* customer_id: int
* customer_age: int
* customer_income: float
* home__ownership: str
* employment_duration: int
* creed_ hist_lenght: int
* historical_default: str

# Loan
* loan_intent: str
* loan_grade: str
* loan_amnt: float
* loan_int_rate: float
* term_years: int
* current_loan_status: str

# Relación
* uno a muchos 
* un cliente puede tener varios prestamos pero un prestamo le pertenece a un cliente

# Entidad Relación


|         Customer          | Relación |            Loan            |
|---------------------------|----------|----------------------------|
| customer_id: int          |          | loan_intent: str           |
| customer_age: int         |          | loan_grade: str            |
| customer_income: float    |          | loan_amnt: float           |
| home__ownership: str      | -\|----<- | loan_int_rate: float       |
| employment_duration: int  |          | term_years: int            |
| creed_ hist_lenght: int   |          | current_loan_status: str   |
| historical_default: str   |          |                            |
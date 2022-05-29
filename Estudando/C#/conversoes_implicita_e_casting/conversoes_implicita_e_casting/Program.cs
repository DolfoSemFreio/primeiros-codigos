using System.Globalization;

int a = 5;
int b = 2;

double resultado = (double) a / b;

Console.WriteLine(resultado.ToString(CultureInfo.InvariantCulture));
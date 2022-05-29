using System.Globalization;

string produto1 = "Computador";
string produto2 = "Mesa de Escritorio";

byte idade = 30;
int codigo = 5290;
char genero = 'M';

double preco1 = 2100.0;
double preco2 = 650.50;
double medida = 53.234567;

Console.WriteLine("Produtos:");
Console.WriteLine($"{produto1}, cujo o preco é R$ {preco1:F2}");
Console.WriteLine($"{produto2}, cujo o preco é R$ {preco2:F2}");
Console.WriteLine();
Console.WriteLine($"Registro: {idade} anos de idade, codigo {codigo} e genero: {genero}");
Console.WriteLine();
Console.WriteLine($"Medida com 8 casas decimais: {medida:F8}");
Console.WriteLine($"Arredondado(tres casas decimais): {medida:F3}");
Console.WriteLine($"Separador decimal invariant culture: {medida.ToString("F3", CultureInfo.InvariantCulture)}");
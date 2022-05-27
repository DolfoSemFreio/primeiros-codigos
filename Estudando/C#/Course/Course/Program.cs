// See https://aka.ms/new-console-template for more information
bool completo = false;
char genero = 'F';  // char comparta apenas um caracter e sempre utilizar aspas simples
char letra = '\u0041'; // Codigo da letra A
byte n1 = 127;
int n2 = 1000;
int n3 = 2147483647;
long n4 = 2147483648L; //colocar um L no final do numero para mostrar q esta trabalhando com o long
float n5 = 4.5f; // colocar f no final do numero para mostrar q é float
double n6 = 4.5;
string nome = "Maria Green"; // usar aspas duplas
object obj1 = "Alex Brown"; // object aceita qualquer coisa
object obj2 = 4.5f;
int menor = int.MinValue;
decimal maior = decimal.MaxValue;

Console.WriteLine(completo);
Console.WriteLine(genero);
Console.WriteLine(letra);
Console.WriteLine(n1);
Console.WriteLine(n2);
Console.WriteLine(n3);
Console.WriteLine(n4);
Console.WriteLine(n5);
Console.WriteLine(n6);
Console.WriteLine(nome);
Console.WriteLine(obj1);
Console.WriteLine(obj2);
Console.WriteLine(menor);
Console.WriteLine(maior);

function esPrimo(num) {
    if (num < 2) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
        if (num % i === 0) return false;
    }
    return true;
}
let inicio = 10;
let fin = 50;
let primos = [];
for (let n = inicio; n <= fin; n++) {
    if (esPrimo(n)) primos.push(n);
}
console.log(`Numeros primos entre ${inicio} y ${fin}: ${primos}`);
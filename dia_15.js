function escribirTexto(texto, delay) {
    let i = 0;
    const intervalo = setInterval(() => {
        if (i < texto.length) {
            process.stdout.write(texto[i]);
            i++;
        } else {
            clearInterval(intervalo);
            console.log("\nTexto completado! :)");
        }
    }, delay);}
const texto = "¡Hola, Tiktok! Este es un efecto genial. 😎";
const velocidad = 100;
console.log("Escribiendo texto...");
escribirTexto(texto, velocidad);
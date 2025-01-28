function dibujarCorazon() {
    const corazon = [ 
        "   **     **   ", " ****** ****** ",  " ************* ", 
        "  ***********  ", "   *********   ", "    *******    ", 
        "     *****     ","      ***      ", "       *       "
    ];
    let i = 0;
    const intervalo = setInterval(() => {
        console.clear();
        console.log("Un corazón para ti. ❤️");
        console.log(corazon.slice(0, i + 1).join("\n"));
        i++;
        if (i === corazon.length) clearInterval(intervalo);
    },300);
};
dibujarCorazon();
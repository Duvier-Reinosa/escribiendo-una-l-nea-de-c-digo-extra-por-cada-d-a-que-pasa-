const express = require('express')
const app = express()
app.get('/fecha/:nombre', (req, res) => {
  const { nombre } = req.params;
  const fecha = new Date().toLocaleString();
  res.json({
    mensaje: `Hola, ${nombre}!`,
    fecha: `La fecha y hora actual es: ${fecha}`
  });
});
app.listen(3000, () => console.log('APi en http://localhost:3000/fecha/{nombre}'))
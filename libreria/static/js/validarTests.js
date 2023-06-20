document
  .getElementById("test-form")
  .addEventListener("submit", function (event) {
    var preguntas = document.getElementsByClassName("test-validar");
    console.table(preguntas);
    for (var i = 0; i < preguntas.length; i++) {
      var opciones = preguntas[i].querySelectorAll('input[type="radio"]');
      var respuestaSeleccionada = false;
      for (var j = 0; j < opciones.length; j++) {
        if (opciones[j].checked) {
          respuestaSeleccionada = true;
          break;
        }
      }
      if (!respuestaSeleccionada) {
        event.preventDefault();
        alert("Por favor, selecciona una respuesta para cada pregunta.");
        return;
      }
    }
  });

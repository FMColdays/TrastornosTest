const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll(".pregunta .input-registro");

const expresiones = {
  usuario: /^[a-zA-Z0-9]{3,20}$/,
  contraseña1: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/,
  contraseña2: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/,
  correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$/,
  edad: /^\d+$/,
};

const campos = {
  id_username: false,
  correo: false,
  contraseña1: false,
  contraseña2: false,
  edad: false,
};

const validarFormulario = (e) => {
  switch (e.target.name) {
    case "username":
      validarCampo(expresiones.usuario, e.target.value, e.target.id);
      break;
    case "correo":
      validarCampo(expresiones.correo, e.target.value, e.target.id);
      break;
    case "password1":
      validarCampo(expresiones.contraseña1, e.target.value, e.target.id);
      validarContraseñas();
      break;
    case "password2":
      validarCampo(expresiones.contraseña2, e.target.value, e.target.id);
      validarContraseñas();
      break;
    case "edad":
      validarCampo(expresiones.edad, e.target.value, e.target.id);
      break;
  }
};

const validarCampo = (expresion, input, campo) => {
  if (expresion.test(input)) {
    document
      .getElementById(`${campo}`)
      .classList.remove("formulario__incorrecto");
    document.getElementById(`${campo}`).classList.add("formulario__correcto");
    campos[campo] = true;
  } else {
    document.getElementById(`${campo}`).classList.add("formulario__incorrecto");
    document
      .getElementById(`${campo}`)
      .classList.remove("formulario__correcto");
  }
};

const validarContraseñas = () => {
  const contraseña1 = document.getElementById("id_password1").value;
  const contraseña2 = document.getElementById("id_password2").value;

  if (contraseña2 !== "") {
    if (contraseña1 !== contraseña2) {
      document.querySelector(".errorE").classList.remove("coincidencia");
      document
        .getElementById("id_password2")
        .classList.add("formulario__incorrecto");
      document
        .getElementById("id_password2")
        .classList.remove("formulario__correcto");
    } else {
      document.querySelector(".errorE").classList.add("coincidencia");
      document
        .getElementById("id_password2")
        .classList.remove("formulario__incorrecto");
      document
        .getElementById("id_password2")
        .classList.add("formulario__correcto");
      campos["contraseña1"] = true;
      campos["contraseña2"] = true;
    }
  }
};

inputs.forEach((input) => {
  input.addEventListener("keyup", validarFormulario);
  input.addEventListener("blur", validarFormulario);
});

formulario.addEventListener("submit", (e) => {
  console.log(campos.id_username)
  console.log(campos.correo)
  console.log(campos.edad)
  console.log(campos.contraseña1)
  console.log(campos.contraseña1)

  if (!campos.id_username ||!campos.correo ||!campos.edad ||!campos.contraseña1 ||!campos.contraseña1) {
    e.preventDefault();
  }
});

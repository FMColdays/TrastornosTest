const formulario = document.getElementById("formulario");
const inputs = document.querySelectorAll(".pregunta .input-registro");

if (document.querySelector(".errorU") && true) {
  document.getElementById("username").addEventListener("input", () => {
    document.querySelector(".errorU").classList.add("disnone");
  });
}

if (document.querySelectorAll(".errorp2") && true) {
  document.getElementById("password2").addEventListener("input", () => {
    document.querySelector(".errorp2").classList.add("disnone");
  });
}


const buscar = (e) =>{
  console.log(e.target.value)
  let palabras = []
 document.querySelectorAll('.buscar').forEach(palabra => {
     palabras = [...palabras, palabra.textContent]
  })
  
  const palabraEncontrada= palabras.filter(palabra => e.target.value === palabra)

  console.log(palabraEncontrada)

}




const expresiones = {
  username: /^[a-zA-Z0-9]{3,20}$/,
  password: /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])[0-9a-zA-Z]{8,}$/,
  correo: /^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-z0-9-.]+$/,
  edad: /^\d+$/,
};

const campos = {
  username: false,
  correo: false,
  password1: false,
  password2: false,
  edad: false,
};

const validarCampo = (expresion, input, campo) => {
  const elemento = document.getElementById(campo);
  elemento.classList.toggle("formulario__incorrecto", !expresion.test(input));
  elemento.classList.toggle("formulario__correcto", expresion.test(input));
  campos[campo] = expresion.test(input);
};

const validarContraseña = () => {
  const contraseña1 = document.getElementById("password1").value;
  const contraseña2 = document.getElementById("password2").value;
  const contraseñaRequisitos = [
    { expresion: /[A-Z]/, campo: "mayusculas" },
    { expresion: /[0-9]/, campo: "numero" },
    { expresion: /^[a-zA-Z0-9\s]*$/, campo: "caracteresEs" },
  ];

  campos.password1 = contraseñaRequisitos.every((req) =>
    req.expresion.test(contraseña1)
  );
  campos.password2 = contraseña1 === contraseña2;

  if (contraseña2 !== "") {
    if (campos.password2) {
      document.querySelector(".errorE").classList.add("coincidencia");
      document
        .getElementById("password2")
        .classList.remove("formulario__incorrecto");
      document
        .getElementById("password2")
        .classList.add("formulario__correcto");
    } else {
      document.querySelector(".errorE").classList.remove("coincidencia");
      document
        .getElementById("password2")
        .classList.remove("formulario__correcto");
      document
        .getElementById("password2")
        .classList.add("formulario__incorrecto");
    }
  }

  const ulRequisitos = document.querySelector(".requisitosPassword");

  let i = 0;
  const listaItems = ulRequisitos.querySelectorAll("li");
  listaItems.forEach((li) => {
    i++;
    if (i === 1 && contraseña1.length > 7) {
      li.classList.add("requisito-correcto");
      minCaracteres = true;
    }
    if (i === 1 && contraseña1.length < 8) {
      li.classList.remove("requisito-correcto");
      minCaracteres = false;
    }
    if (i === 2 && /[A-Z]/.test(contraseña1)) {
      li.classList.add("requisito-correcto");
      mayusculas = true;
    } else if (i === 2 && !/[A-Z]/.test(contraseña1)) {
      li.classList.remove("requisito-correcto");
      mayusculas = false;
    }
    if (i === 3 && /[0-9]/.test(contraseña1)) {
      li.classList.add("requisito-correcto");
      numero = true;
    } else if (i === 3 && !/[0-9]/.test(contraseña1)) {
      li.classList.remove("requisito-correcto");
      numero = false;
    }
    if (i === 4 && /^[a-zA-Z0-9\s]*$/.test(contraseña1)) {
      li.classList.add("requisito-correcto");
      caracteresEs = true;
    } else if (i === 4 && !/^[a-zA-Z0-9\s]*$/.test(contraseña1)) {
      li.classList.remove("requisito-correcto");
      caracteresEs = false;
    }
  });

  if (minCaracteres && mayusculas && numero && caracteresEs) {
    campos.password1 = true;
  } else {
    campos.password1 = false;
  }
};

const validarFormulario = (e) => {
  const campo = e.target.name;
  const valor = e.target.value;
  switch (campo) {
    case "username":
    case "correo":
    case "edad":
      validarCampo(expresiones[campo], valor, campo);
      break;
    case "password1":
    case "password2":
      validarCampo(expresiones.password, valor, campo);
      validarContraseña();
      break;
  }
};

inputs.forEach((input) => {
  input.addEventListener("keyup", validarFormulario);
  input.addEventListener("blur", validarFormulario);
});

formulario.addEventListener("submit", (e) => {
  if (Object.values(campos).some((campo) => !campo)) {
    e.preventDefault();
  }
});

document.addEventListener("DOMContentLoaded", function () {
  const formularioCalimaco = document.getElementById("formXLSX");
  const formularioGestionRW = document.getElementById("formXLSX_RW");

  formularioCalimaco.addEventListener("submit", async (e) => {
    e.preventDefault(); // Evita que el formulario se envíe automáticamente

    await handleSubmit(formularioCalimaco, "/subir-data-xlsx");
  });

  formularioGestionRW.addEventListener("submit", async (e) => {
    e.preventDefault(); // Evita que el formulario se envíe automáticamente

    await handleSubmit(formularioGestionRW, "/subir-data-xlsx-rw");
  });

  async function handleSubmit(formulario, url) {
    myLoading(true);

    const formData = new FormData(formulario);
    const headers = {
      "Content-Type": "multipart/form-data",
    };

    try {
      const response = await axios.post(url, formData, { headers });

      // Manejar la respuesta del servidor aquí
      const { status_server, message } = response.data;

      if (!status_server) {
        console.log(`HTTP error! status: ${status_server} 😭`);
      }

      if (status_server == "success") {
        console.log(status_server, message);

        setTimeout(function () {
          myLoading(false);
          alerta(message, 1);
        }, 3000);
      } else {
        alerta(message, 0);
      }
    } catch (error) {
      // Manejar errores aquí
      console.error(error);
    }
  }

  /**
   * Función para mostrar/ocultar el loader
   */
  let preventReload = false; // Variable para controlar la prevención de recarga
  function myLoading(loading) {
    let loadingElement = document.querySelector(".contentLoading");
    let body = document.body;

    if (loading) {
      loadingElement.style.display = "flex";
      body.style.overflow = "hidden";

      // Activa la prevención de recarga
      preventReload = true;
    } else {
      // Desactiva la prevención de recarga
      preventReload = false;
      loadingElement.style.display = "none";
      body.style.overflow = "";
    }
  }

  /**
   * Función para mostrar una alerta temporal
   */
  function alerta(msj, tipo_msj) {
    const divExistente = document.querySelector(".alert");
    if (divExistente) {
      divExistente.remove();
    }

    // Crear un nuevo div para la alerta
    const divRespuesta = document.createElement("div");

    divRespuesta.innerHTML = `
      <div class="alert ${
        tipo_msj == 1 ? "alert-success" : "alert-danger"
      }  alert-dismissible text-center" role="alert" style="font-size: 20px;">
        ${msj}
      </div>
    `;

    setTimeout(function () {
      divRespuesta.innerHTML = "";
    }, 3000);

    // Agregar el div al final del contenedor con clase "container"
    const container = document.querySelector("#respuesta");
    container.insertAdjacentElement("beforeend", divRespuesta);
  }
});

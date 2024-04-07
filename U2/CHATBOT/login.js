document.addEventListener('DOMContentLoaded', function() {
    var loginFormContainer = document.getElementById('loginFormContainer');
    var registroLink = document.getElementById('registroLink');
    var registroFormContainer = document.getElementById('registroFormContainer');
    var volverLink = document.getElementById('volverLink');
    var olvidoLink = document.getElementById('olvidoLink');
    var recuperacionFormContainer = document.getElementById('recuperacionFormContainer');
    var volverLinkRecuperacion = document.getElementById('volverLinkRecuperacion');

    // Mostrar el formulario de registro cuando se hace clic en el enlace
    registroLink.addEventListener('click', function(event) {
        event.preventDefault();
        loginFormContainer.style.display = 'none';
        registroFormContainer.style.display = 'block';
    });

    // Volver al formulario de inicio de sesión desde el formulario de registro
    volverLink.addEventListener('click', function(event) {
        event.preventDefault();
        registroFormContainer.style.display = 'none';
        loginFormContainer.style.display = 'block';
    });

    // Mostrar el formulario de recuperación de contraseña cuando se hace clic en el enlace
    olvidoLink.addEventListener('click', function(event) {
        event.preventDefault();
        loginFormContainer.style.display = 'none';
        recuperacionFormContainer.style.display = 'block';
    });

    // Volver al formulario de inicio de sesión desde el formulario de recuperación de contraseña
    volverLinkRecuperacion.addEventListener('click', function(event) {
        event.preventDefault();
        recuperacionFormContainer.style.display = 'none';
        loginFormContainer.style.display = 'block';
    });

    // Manejar el envío del formulario de registro
    var registerForm = document.getElementById('registerForm');
    registerForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Obtener valores del formulario de registro
        var regUsername = document.getElementById('regUsername').value;
        var regPassword = document.getElementById('regPassword').value;

        // Verificar si el usuario ya existe en el almacenamiento local
        if (localStorage.getItem(regUsername) !== null) {
            alert('El usuario ya existe. Por favor, elige otro nombre de usuario.');
        } else {
            // Guardar usuario y contraseña en el almacenamiento local
            localStorage.setItem(regUsername, regPassword);
            alert('Usuario registrado exitosamente.');

            // Limpiar el formulario
            registerForm.reset();

            // Volver al formulario de inicio de sesión
            registroFormContainer.style.display = 'none';
            loginFormContainer.style.display = 'block';
        }
    });

    // Manejar el envío del formulario de recuperación de contraseña
    var recuperacionForm = document.getElementById('recuperacionForm');
    recuperacionForm.addEventListener('submit', function(event) {
        event.preventDefault();

        var recUsername = document.getElementById('recUsername').value;

        var newPass = prompt('Ingrese una nueva contraseña para ' + recUsername + ':');

        if (newPass) {
            // Guardar la nueva contraseña en el almacenamiento local
            localStorage.setItem(recUsername, newPass);
            alert('La contraseña para el usuario ' + recUsername + ' ha sido actualizada correctamente.');
        } else {
            alert('No se ha ingresado una nueva contraseña.');
        }
    });

    // Manejar el envío del formulario de inicio de sesión
    var loginForm = document.getElementById('loginForm');
    loginForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Obtener valores del formulario de inicio de sesión
        var username = document.getElementById('username').value;
        var password = document.getElementById('password').value;

        // Verificar si las credenciales son válidas
        var storedPassword = localStorage.getItem(username);
        if (storedPassword === password) {
            // Credenciales válidas, redirigir al usuario a la página de inicio
            window.location.href = 'inicio.html';
        } else {
            // Credenciales incorrectas, mostrar mensaje de error
            alert('Credenciales incorrectas. Por favor, inténtalo de nuevo.');
        }
    });
});

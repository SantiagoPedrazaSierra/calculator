document.addEventListener('DOMContentLoaded', function () {
    const resultField = document.getElementById('result');
    const buttons = document.querySelectorAll('.btn');

    buttons.forEach(button => {
        button.addEventListener('click', function () {
            const value = this.getAttribute('data-value');
            let currentValue = resultField.value;

            if (value === 'C') {
                // Limpiar el campo de expresión
                resultField.value = '';
            } else if (value === '=') {
                // No hacer nada porque el formulario ya se envía al hacer clic en "="
                // El servidor evaluará la expresión.
            } else {
                // Agregar el valor del botón al campo de expresión
                resultField.value += value;
            }
        });
    });
});

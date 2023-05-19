document.getElementById('id_plate').addEventListener('change', function() {
    var plate = this.value;

    // Realiza una solicitud AJAX para obtener el tipo de vehículo según el ID del vehículo seleccionado
    $.ajax({
        url: '/api/vehicle-label/',  // URL de la vista que obtiene el tipo de vehículo según el ID del vehículo
        data: { plate : plate},
        dataType: 'json',
        success: function(response) {
            var label = response.label;
            document.getElementById('id_emissions').value = label
            document.getElementById('id_emissions').type = "text"
        },
    });
});

document.getElementById('id_university').addEventListener('change', function() {
    var universityId = this.value;
    
    $.ajax({
        url: '/api/parkings/',  
        data: { university_id: universityId },
        dataType: 'json',
        success: function(data) {
            var parkingsSelect = document.getElementById('id_parking');
            parkingsSelect.innerHTML = '';
            for (var i = 0; i < data.length; i++) {
                var option = document.createElement('option');
                option.value = data[i].id;
                option.text = data[i].name;
                parkingsSelect.appendChild(option);
            }
        },
        error: function() {
            console.log('Error al obtener los parkings');
        }
    });
});

document.getElementById('id_parking').addEventListener('change', function() {
    var parkingId = this.value;
    var vehicleType = document.getElementById('id_vehicle').value;

    $.ajax({
        url: '/api/parking-spots/', 
        data: { parking_id: parkingId, vehicle_type: vehicleType },
        dataType: 'json',
        success: function(data) {
            var parkingSpotsSelect = document.getElementById('id_parking_spot');
            parkingSpotsSelect.innerHTML = '';
            for (var i = 0; i < data.length; i++) {
                var option = document.createElement('option');
                option.value = data[i].id;
                option.text = data[i].id;
                parkingSpotsSelect.appendChild(option);
            }
        },
        error: function() {
            console.log('Error al obtener los parking spots');
        }
    });
});

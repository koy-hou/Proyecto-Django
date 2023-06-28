//Modo oscuro
$(document).ready(function() {
  var isChecked = localStorage.getItem("modoOscuro");

  if (isChecked === 'true') {
    $("modoOscuro").prop('checked', true);
    setDarkMode(true);
  }

  $('#modoOscuro').click(function() {
    var isChecked = $(this).is(':checked');

    localStorage.setItem('modoOscuro', isChecked);

    setDarkMode(isChecked);
  });
});

function setDarkMode(isDarkMode) {
  if (isDarkMode) {
    $(".headerPag").css({"background-color":"#151515"})
    $(".navbar").css({"background-color":"#151515"})
    $("body").css({"background-color":"#331847"})
    $("body").css({"color":"antiquewhite"})
    $(".tarjetas").css({"background-color":"#151515"});
  } else {  
    $(".headerPag").css({"background-color":"#F98404"})
    $(".navbar").css({"background-color":"#F98404"})
    $("body").css({"background-color":"white"})
    $("body").css({"color":"black"})
    $(".tarjetas").css({"background-color":"transparent"});
  }
}

//Reloj
$(document).ready(function() {
    var url = "http://worldtimeapi.org/api/timezone/Europe/Madrid";
  
    
    function horaLocal() {
      
      $.getJSON(url, function(data) {
        
        var fecha = new Date(data.datetime);
        var hora = fecha.toLocaleTimeString();
        $("#hora").text("Hora Santiiago Chile: "+hora);
      });
    }
    
    setInterval(horaLocal, 1000);
  });

  //Clima
  const apiKeyClima = '89be60e3ae71b61c91494529716b226d'; // Tu propia clave de API de OpenWeather
  const city = 'Santiago';

  const apiUrl = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${apiKeyClima}`;

  $(document).ready(function() {
    obtenerClima();
  
    function obtenerClima() {
      $.getJSON(apiUrl, function(data) {
        const temperaturaKelvin = data.main.temp;
        const temperaturaCelsius = temperaturaKelvin - 273.15;
        const descripcion = data.weather[0].description;
        const icono = data.weather[0].icon;
  
        const iconoUrl = `https://openweathermap.org/img/w/${icono}.png`;
  
        $('#clima').html(`
          <p style="padding-left: 10px;">Temperatura de Santiago de Chile: ${temperaturaCelsius.toFixed(2)} °C <img src="${iconoUrl}" alt="Icono del clima" width="30" height="30"></p>
          
        `);
      })
      .fail(function(error) {
        console.log(error);
      });
    }
  });


  //Api Nasa 

  const apiKey = 'xrvFhOeI5gldaxPQqfTStJDX6DXLZWMONb8aiwTR';
  const url = `https://api.nasa.gov/planetary/apod?api_key=${apiKey}`;
  const urlNasa = 'https://api.nasa.gov/neo/rest/v1/feed';

  //Foto del dia
  $(document).ready(function() {
    
    $.get(url, function(data) {
      let html = `
        <img src="${data.url}" alt="${data.title}" style="max-width: 100%;">
        <h2>${data.title}</h2>
        <br>
        <p style="font-weight: bold;  font-size: 20px;">${data.explanation}</p>
      `;
      
      $('#apod').html(html);
    })
    .fail(function(error) {
      console.log(error);
    });
  });

  //Asteroides cercanos
  const imgPeligro = '<img src="img/peligro.svg" alt="Peligroso" width="30" height="24">';
  const imgNoPeligro = '<img src="img/nopeligro.svg" alt="No peligroso" width="30" height="24">';

  $(document).ready(function() {
    $('#fetchData').click(function() {
      $.get(urlNasa, { api_key: apiKey })
        .done(function(data) {
          let formattedData = '';
          for (const date in data.near_earth_objects) {
            formattedData += `<p>Fecha: ${date}</p>`;
            const neoObjects = data.near_earth_objects[date];
            neoObjects.forEach(function(neo, index) {
              formattedData += `<p>Asteroid ${index + 1}:</p>`;
              formattedData += `<p>&nbsp;Nombre: ${neo.name}</p>`;
              formattedData += `<p>&nbsp;Diámetro: ${neo.estimated_diameter.kilometers.estimated_diameter_max} km</p>`;
              formattedData += `<p>&nbsp;Peligroso: ${neo.is_potentially_hazardous_asteroid ? `Sí ${imgPeligro}` : `No ${imgNoPeligro}`}</p>`;
              formattedData += `<hr><br>`
            });
          }
          $('#neoData').html(formattedData);
        })
        .fail(function(error) {
          console.log(error);
        });
    });
  });
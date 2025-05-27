let timeout;

function clean_msg() {
  document.getElementById('submit_confirmation').style.transition = "opacity 0.3s linear";
  document.getElementById('submit_confirmation').style.opacity = 0;
}
function store_values(Name, Date, Notes) {
  if (Notes == '') {
    Notes = null;
  }
  const appointment = {                  
    name: Name,
    date: Date,
    notes: Notes,
  }

  fetch('http://localhost:8000/appointments', {
    method: 'POST',                       // 1. HTTP method: POST (can also be GET, PUT, DELETE, etc.)
    headers: {
      'Content-Type': 'application/json', // 2. Tells the server we're sending JSON
    },
    body: JSON.stringify(appointment),    // 3. Convert a JS object to JSON
  })
  .then(response => response.json())      // 4. Parse the response as JSON
  .then(data => console.log(data))        // 5. Do something with the response
  .catch(error => console.error(error));  // 6. Handle any errors
}

function open_new_appointment() {
  document.getElementById("new_appointment").style.display = "block";
}

function close_new_appointment() {
  document.getElementById("new_appointment").style.display = "none";
}

function submit() {
  const name = document.getElementById('name').value.trim();
  const date = document.getElementById('date').value;
  const notes = document.getElementById('notes').value.trim();
  if (name !== "" && date !== "") {
    store_values(name, date, notes)
    document.getElementById('name').value = '';
    document.getElementById('date').value = '';
    document.getElementById('notes').value = '';
    document.getElementById('submit_confirmation').innerHTML = 'good boy';
    document.getElementById('submit_confirmation').style.color = '#1c9c3e';
  } else {
    document.getElementById('submit_confirmation').innerHTML = 'prenche bem essa merda';
    document.getElementById('submit_confirmation').style.color = '#dd4a4a';
  }

  clearTimeout(timeout);
  document.getElementById('submit_confirmation').style.transition = "none";
  document.getElementById('submit_confirmation').style.opacity = 1;
  timeout = setTimeout(clean_msg, 3000);
}

if (document.getElementById("appointment").style.width){

  
}

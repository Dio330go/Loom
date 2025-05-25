let timeout;

function clean_msg() {
  document.getElementById('submit_confirmation').innerHTML = '<br>';
}

function store_values() {
  
}

function submit() {
  const name = document.getElementById('name').value.trim();
  const date = document.getElementById('date').value.trim();

  if (name !== "" && date !== "") {
    document.getElementById('name').value = '';
    document.getElementById('date').value = '';
    document.getElementById('submit_confirmation').innerHTML = 'o teu apointment ja ta bue guardado';
    document.getElementById('submit_confirmation').style.color = '#1c9c3e';
    store_values()
  } else {
    document.getElementById('submit_confirmation').innerHTML = 'prenche bem essa merda';
    document.getElementById('submit_confirmation').style.color = '#dd4a4a';
  }

  clearTimeout(timeout);
  timeout = setTimeout(clean_msg, 3000);
}




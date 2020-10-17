document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#login_btn').addEventListener('click', () => load_home());
  document.querySelector('#register_btn').addEventListener('click', () => load_history());

  // By default, load the inbox
  load_home();
});

function load_home()
{
    document.querySelector('#login').style.display = 'block';
    document.querySelector('#register').style.display = 'none';
}

function load_history()
{
    document.querySelector('#login').style.display = 'none';
    document.querySelector('#register').style.display = 'block';	
}
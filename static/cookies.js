function getCookieValue(name) {
  let result = document.cookie.match("(^|[^;]+)\\s*" + name + "\\s*=\\s*([^;]+)")
  return result ? result.pop() : ""
}

  window.onload = function check_cookies() 
  {
    var accepted = getCookieValue("cookie-accept") == "true"
    if (accepted != true) 
    {
      var div_cookie = document.getElementById("cookie"); 
      div_cookie.innerHTML = '<div>Používáme cookies pro zlepšení našich služeb.<br><a href="/cookies">Více informací</a></div><form onsubmit="accept_cookies()"><button class="col-1">Přijmout</button></form>'
    } 
  }

  function accept_cookies()
  {
    document.cookie = "cookie-accept=true";
    var div_cookie = document.getElementById("cookie"); 
    div_cookie.parentNode.removeChild(div_cookie);
  }
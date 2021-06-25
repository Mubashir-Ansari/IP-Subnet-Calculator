// Triggering function of py by passing Querry through JS
function main() {
    var ipadd = document.getElementById("data_1").value;
    eel.main(ipadd);
  }
eel.expose(IPclass);
  function IPclass(ans){
    document.getElementById("class").value = ans
    }
eel.expose(subnett);
function subnett(ans){
  document.getElementById("subnet").value = ans
  }
eel.expose(wildcard);
  function wildcard(ans){
    document.getElementById("wild").value = ans
    
  }
eel.expose(broadcast);
  function broadcast(ans){
    document.getElementById("broad").value = ans
  }
eel.expose(firstnet);
  function firstnet(ans){
    document.getElementById("first").value = ans
  }
eel.expose(lastnet);
  function lastnet(ans){
    document.getElementById("last").value = ans
  }
eel.expose(nextnet);
  function nextnet(ans){
    document.getElementById("next").value = ans
  }
eel.expose(cidr);
  function cidr(ans){
    document.getElementById("cidr").value = ans
  }
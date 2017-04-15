function User(){
  var that = this;
  this.set_username = function(e){
    var un = e.target.value;
    if (un.length > 3 && un.length < 31){
      that.username = un;
    }
    else if (that.username){
      delete that.username;
    }
    enable_submit();
  };

  this.set_password = function(e){
    var pw = e.target.value; 
    if (pw.length > 5 && pw.length < 31){
      that.password = pw;
    }
    else if (that.password){
      delete that.password;
    }
    that.set_confirm(e);
    enable_submit();
  };

  this.set_confirm = function(e){
    var pw = e.target.value;
    if (that.password && pw === that.password){
      that.cf = true;
    }
    else{
      that.cf = false;
    }
    enable_submit();
  };

  function enable_submit(){
    if (that.password && that.username && that.cf){
      document.getElementsByClassName('submit')[0].disabled = false;
    }
    else{
      document.getElementsByClassName('submit')[0].disabled = true;
    }
  }
}

var user = new User();

window.onload = function(){
  document.getElementsByClassName('submit')[0].disabled = true;
  document.getElementsByClassName('username')[0].onchange = user.set_username;
  document.getElementsByClassName('password')[0].onchange = user.set_password;
  document.getElementsByClassName('password')[1].onchange = user.set_confirm;
};

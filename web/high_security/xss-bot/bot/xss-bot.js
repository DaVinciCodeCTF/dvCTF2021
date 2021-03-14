var page = require('webpage').create();
var host = "web";
var url = "http://"+host+":5000/security";
var timeout = 2000;
phantom.addCookie({
      'name': 'flag',
      'value': 'dvCTF{xss_l0ve<3}',
      'domain': host,
      'path': '/',
      'httponly': false
});

phantom.addCookie({
      'name': 'session',
      'value': '.eJyrVkpMyc3MU7Iy1FHKTAFTOfnp6akp8SDBkqLSVB2l0uLUorzE3FQlK6jiWgDXuRHC.YEviKQ.PSCKIp3-FFTah9foah5XEN33Mk4',
      'domain': host,
      'path': '/',
      'httponly': false
});
page.onNavigationRequested = function(url, type, willNavigate, main) {
      console.log("[URL] URL="+url);  
};
page.settings.resourceTimeout = timeout;
page.onResourceTimeout = function(e) {
      setTimeout(function(){
                console.log("[INFO] Timeout")
                phantom.exit();
            }, 1);
};
page.open(url, function(status) {
      console.log("[INFO] rendered page");
      setTimeout(function(){
                phantom.exit();
            }, 1);
});

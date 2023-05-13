// This code enables form submissions to be handled asynchronously without a page reload, and
// provides user feedback based on the outcome of the form submission.
// This code is used on the Notary page.


$(document).ready(function() {
    const trackingCookieNameMap = {
      _mkto_trk: "marketo"
    };
  
    function collectEnterpriseTrackingCookies() {
      const cookies = document.cookie.split("; ").reduce(function(acc, cookie) {
        const splitCookie = cookie.split("=");
        const name = splitCookie[0];
        if (name in trackingCookieNameMap) {
          const mappedName = trackingCookieNameMap[name];
          const value = splitCookie.slice(1).join("=");
          acc[mappedName] = value;
        }
        return acc;
      }, {});
      return cookies;
    }
  
    $('form').on('submit', function(e) {
      e.preventDefault();
      const form = $(this);
      const payload = {};
  
      form.find('input, textarea, select').each(function() {
        const field = $(this);
        const name = field.attr('name');
        const value = field.val();
        if (name) {
          payload[name] = value;
        }
      });
  
      const data = {
        form: form,
        payload: payload,
        success: false
      };
  
      submitForm(data);
    });
  
    function submitForm(data) {
      $.ajax({
        type: 'POST',
        url: data.form.attr('action'),
        data: data.payload
      })
      .done(function() {
        data.success = true;
        afterSubmit(data);
      })
      .fail(function() {
        data.success = false;
        afterSubmit(data);
      });
    }
  
    function afterSubmit(data) {
      const form = data.form;
      const success = data.success;
      const successMessage = form.find('.success-message');
      const errorMessage = form.find('.error-message');
  
      if (success) {
        successMessage.show();
        errorMessage.hide();
      } else {
        successMessage.hide();
        errorMessage.show();
      }
      form.find('input, textarea, select').val('');
    }
  });
  
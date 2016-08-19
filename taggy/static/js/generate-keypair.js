/**
 * Created by michel on 19/08/16.
 */

var generateStep = $('#generate-container');
var encryptStep = $('#encrypt-container');
var uploadedStep = $('#uploaded-container');

var progressIndicator = $('.progress-indicator');

var privateKey = null;

var uploadForm = $('#upload-form');


$('#private-key-password-form').submit(function (event) {
    event.preventDefault();
    if (validateForm()) {
        encryptKey(function () {
            $.post(uploadForm.attr('action'), uploadForm.serialize(), function () {
                encryptStep.addClass('hidden');
                uploadedStep.removeClass('hidden');
            });
        });
    }
});


$('#generate-keypair').click(function () {
    $(this).addClass('hidden');
    generateKeys(function () {
        generateStep.addClass('hidden');
        encryptStep.removeClass('hidden');
    });
});

var encryptKey = function (readyHandler) {
    triplesec.encrypt({

        data: new triplesec.Buffer(privateKey),
        key: new triplesec.Buffer($('#encrypt-password').val()),
        progress_hook: function (obj) {
            console.log(obj);
        }

    }, function (err, buff) {

        if (!err) {
            $('#private-key').val(buff.toString('hex'));
            readyHandler();
        } else {
            console.log(err);
        }

    });

};


var generateKeys = function (readyHandler) {
    var sKeySize = '4096';  // $('#key-size').attr('data-value');
    var keySize = parseInt(sKeySize);
    var crypt = new JSEncrypt({default_key_size: keySize});
    var async = true;  // $('#async-ck').is(':checked');
    var dt = new Date();
    var time = -(dt.getTime());
    if (async) {
        $('#time-report').text('.');
        var load = setInterval(function () {
            var text = progressIndicator.text();
            progressIndicator.text(text + '.');
        }, 500);
        crypt.getKey(function () {
            clearInterval(load);
            dt = new Date();
            time += (dt.getTime());
            // $('#time-report').text('Generated in ' + time + ' ms');
            privateKey = crypt.getPrivateKey();
            $('#public-key').val(crypt.getPublicKey());
            readyHandler();
        });
    } else {
        crypt.getKey();
        dt = new Date();
        time += (dt.getTime());
        // $('#time-report').text('Generated in ' + time + ' ms');
        privateKey = crypt.getPrivateKey();
        $('#public-key').val(crypt.getPublicKey());
        readyHandler();
    }
};

var validateForm = function () {
    // TODO form validation
    return true
};

generateStep.removeClass('hidden');

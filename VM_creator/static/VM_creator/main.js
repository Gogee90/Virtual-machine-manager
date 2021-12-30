document.addEventListener("DOMContentLoaded", function () {
    var elems = document.querySelectorAll("select");
    var options = document.querySelectorAll("option");
    var instances = M.FormSelect.init(elems, options);
});

let config = document.getElementById("id_configuration");
let pool = document.getElementById("id_pool");
let division = document.getElementById("id_division");
let number_of_cores = document.getElementById("id_cpu_cores");
let ram_capacity = document.getElementById("id_ram_capacity");
let hdd_capacity = document.getElementById("id_hdd_capacity");
let id_name = document.getElementById("id_name");
let submit_btn = document.getElementById("id_submit_btn");
let log = document.getElementById("log");

let selectedConfigText = null;
let selectedPoolText = null;
let vmNameText = null;

let maskOptions = {
    mask: "aaaaaaaaaaaaaaaa-{#}",
    prepare: (str) => {
        return str.toUpperCase();
    },
};

let mask = IMask(id_name, maskOptions);

config.addEventListener("change", function () {
    selectedConfigText = this.options[this.selectedIndex].text;
    let selectedOptionValue = this.value;
    fetch(`http://vm-manager.francecentral.cloudapp.azure.com/get-configuration/${selectedOptionValue}`)
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            number_of_cores.value = data.config.number_of_cores;
            ram_capacity.value = data.config.ram_capacity;
            hdd_capacity.value = data.config.hdd_capacity;
        });
});

pool.addEventListener("change", function () {
    selectedPoolText = this.options[this.selectedIndex].text;
});

id_name.addEventListener("keydown", (event) => {
    vmNameText = event.path[0].value;
});

submit_btn.addEventListener("click", function (event) {
    const Notify = new XNotify();
    let is_done = false;
    let textarea = document.createElement("textarea");
    let socket = new WebSocket("ws://vm-manager.francecentral.cloudapp.azure.com/ws/");
    let messages = 'Начинаем создание виртуальной машины ... это займёт какое-то время';
    if (is_done == false) {
        event.preventDefault();
        SlickLoader.enable();
        submit_btn.disabled = true;
        log.append(textarea);
        textarea.innerHTML = messages;
        textarea.disabled = true;
        socket.onopen = () => {
            socket.send([vmNameText, selectedPoolText, selectedConfigText]);
        };
        socket.onmessage = function (event) {
            console.log(event);
            messages += '\n' + event.data.split('\n');
            textarea.innerHTML = messages;
            textarea.scrollTop = textarea.scrollHeight;
        };
        socket.onclose = (event) => {
            if (event.wasClean) {
                SlickLoader.disable();
                Notify.success({
                    title: "Успех",
                    description: "Виртуальная машина успешно создана"
                });
                setTimeout(function () {
                    document.forms["vm-create-form"].submit();
                }, 10000);
            } else {
                SlickLoader.disable();
                Notify.error({
                    title: "Ошибка",
                    description: "Возникла ошибка при создании машины"
                });
            }
        };
    }
});

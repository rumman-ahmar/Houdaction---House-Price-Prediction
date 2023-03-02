let getNumValues = (value) => {
    return (value === "Yes") ? 1 : 0;
}

let getPredictedPrice = (e) => {
    e.preventDefault();
    let city = document.getElementById('city').value;
    let underConstruction = document.getElementById('under-construction').value;
    let bhk = document.getElementById('bhk').value;
    let area = document.getElementById('area').value;;
    let rtm = document.getElementById('rtm').value;
    let predictedPrice = document.getElementById('predicted-price');
    let bhkAlert = document.getElementById('bhk-alert');
    let areaAlert = document.getElementById('area-alert');

    if (bhk == ''){
        bhkAlert.innerHTML = "<div class='alert alert-danger' role=alert'>Please enter BHK</div>"
        return false;
    }
    else{
        bhkAlert.innerHTML = ''
    }

    if (area < 500){
        areaAlert.innerHTML = "<div class='alert alert-danger' role=alert'>Area Squre Foot must be greater than 500</div>"
        return false;
    }
    else{
        areaAlert.innerHTML = ''
    }


    // change value
    underConstruction = getNumValues(underConstruction)
    rtm = getNumValues(rtm)

    url = `/predict_price?city=${city}&under_construction=${underConstruction}&bhk=${parseInt(bhk)}&sqr_ft=${parseFloat(area)}&rtm=${rtm}`

    fetch(url)
        .then((response) => response.json()
            .then((data) => ({ status: response.status, price: data })))
        .then((data) => {
            if (data.status === 200) {
                predictedPrice.innerHTML = `<b>${data.price}</b>`;
            }
            else {
                predictedPrice.innerHTML = `<b>Something went wrong</b>`;
            }
        })
        .catch((error) => {
            predictedPrice.innerHTML = `<b>Something went wrong</b>`;
        });
}


let getCities = () => {

    let citiesHTML = ''
    let city = document.getElementById('city');
    fetch("/cities")
        .then((response) => response.json())
        .then((cities) => {

            cities.forEach(city => {
                citiesHTML += `<option value="${city}">${city}</option>`
            });
            city.innerHTML = citiesHTML
        });
}
getCities();
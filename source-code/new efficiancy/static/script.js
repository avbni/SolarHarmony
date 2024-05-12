function showInput() {
  
  const inputContainer = document.getElementById("inputContainer");
  const electricityCost = document.getElementById("electricityCost");
  const electricityCostSlider = document.getElementById("electricityCostSlider");
  const unitsconsumed = document.getElementById("unitsconsumed");
  const unitsconsumedslider = document.getElementById("unitsconsumedslider");
  const roofarea = document.getElementById("roofarea");
  const roofareaslider = document.getElementById("roofareaslider");
  const budget = document.getElementById("budget");
  const budgetslider = document.getElementById("budgetslider");
  const slider = document.getElementById("slider");
  const sliderContainer = document.getElementById("sliderContainer");



  inputContainer.innerHTML = "";
  sliderContainer.classList.add("hidden");

   {
    sliderContainer.classList.remove("hidden");
    roofareaslider.min = 100;
    roofareaslider.max = 1000;
    roofareaslider.step = 10;
    roofareaslider.value = 100;
  } 
  {
    sliderContainer.classList.remove("hidden");
    budgetslider.min = 1000;
    budgetslider.max = 10000;
    budgetslider.step = 100;
    budgetslider.value = 1000;
  }  
  {
    sliderContainer.classList.remove("hidden");
    electricityCostSlider.min = 1;
    electricityCostSlider.max = 10;
    electricityCostSlider.step = 0.5;
    electricityCostSlider.value = 5;
  }
  {
    sliderContainer.classList.remove("hidden");
    unitsconsumedslider.min = 1;
    unitsconsumedslider.max = 10;
    unitsconsumedslider.step = 0.5;
    unitsconsumedslider.value = 5;
  }
}



function showFlatsInput() {
  const category = document.getElementById("category").value;
  const flatsInput = document.getElementById("flatsInput");

  if (category === "apartment") {
    flatsInput.innerHTML = `
      <label for="flats">Number of Flats:</label>
      <input type="number" id="flats" min="1" value="1">
    `;
  } else {
    flatsInput.innerHTML = "";
  }
}


document.getElementById("electricityCost").addEventListener("input", function() {
  document.getElementById("electricityCostSlider").value = this.value;
});

document.getElementById("electricityCostSlider").addEventListener("input", function() {
  document.getElementById("electricityCost").value = this.value;

});

document.getElementById("roofarea").addEventListener("input", function() {
  document.getElementById("roofareaslider").value = this.value;
});
document.getElementById("roofareaslider").addEventListener("input", function() {
  document.getElementById("roofarea").value = this.value;
});

document.getElementById("unitsconsumedslider").addEventListener("input", function() {
  document.getElementById("unitsconsumed").value = this.value;
});
document.getElementById("unitsconsumed").addEventListener("input", function() {
  document.getElementById("unitsconsumedslider").value = this.value;
});

document.getElementById("budgetslider").addEventListener("input", function() {
  document.getElementById("budget").value = this.value;
});
document.getElementById("budget").addEventListener("input", function() {
  document.getElementById("budgetslider").value = this.value;
});

document.getElementById("unitsconsumedslider").addEventListener("input", function() {
  document.getElementById("unitsconsumed").value = this.value;
});
document.getElementById("unitsconsumed").addEventListener("input", function() {
  document.getElementById("unitsconsumedslider").value = this.value;
});




// function calculate() {
//   const option = document.getElementById("option").value;
//   let result = "";

//   if (option === "1") {
//     const rooftopArea = parseFloat(document.getElementById("slider").value);
//     result = `You entered Total Rooftop Area: ${rooftopArea} sq ft`;
//   } else if (option === "2") {
//     const panelCapacity = parseFloat(document.getElementById("slider").value);
//     result = `You entered Solar Panel Capacity: ${panelCapacity} kW`;
//   } else if (option === "3") {
//     const budget = parseFloat(document.getElementById("slider").value);
//     result = `You entered Budget: $${budget}`;
//   } else if (option === "4") {
//     const electricityCost = parseFloat(document.getElementById("electricityCost").value);
//     result = `You entered Average Electricity Cost: ₹${electricityCost} per KWh`;
//   }

//   const category = document.getElementById("category").value;
//   result += `, Category: ${category}`;
//   document.getElementById("result").innerText = result;
// }




// function showInput() {
//   const option = document.getElementById("option").value;
//   const inputContainer = document.getElementById("inputContainer");
//   const sliderContainer = document.getElementById("sliderContainer");
//   // const slider = document.getElementById("slider");
//   const electricityCostSlider = document.getElementById("electricityCostSlider");

//   inputContainer.innerHTML = "";
//   sliderContainer.classList.add("hidden");



//   if (option === "1") {
//     sliderContainer.classList.remove("hidden");
//     document.getElementById("slider").min = 100;
//     document.getElementById("slider").max = 1000;
//     document.getElementById("slider").step = 10;
//     document.getElementById("slider").value = 100;
//     // document.getElementById("sliderValue").innerText = slider.value;

//   } else if (option === "2") {
//     sliderContainer.classList.remove("hidden");
//     document.getElementById("slider").min = 1;
//     document.getElementById("slider").max = 10;
//     document.getElementById("slider").step = 1;
//     document.getElementById("slider").value = 1;
//     // document.getElementById("sliderValue").innerText = slider.value;

//   } else if (option === "3") {
//     sliderContainer.classList.remove("hidden");
//     document.getElementById("slider").min = 1;
//     document.getElementById("slider").max = 10;
//     document.getElementById("slider").step = 1;
//     document.getElementById("slider").value = 1;
//     // document.getElementById("sliderValue").innerText = slider.value;
 
//   } else if (option === "4") {
//     sliderContainer.classList.remove("hidden");
//     electricityCostSlider.min = 1;
//     electricityCostSlider.max = 10;
//     electricityCostSlider.step = 0.5;
//     electricityCostSlider.value = 5;
//     document.getElementById("electricityCost").value = electricityCostSlider.value;
   
//   }
// }


// function calculate() {
//   const option = document.getElementById("option").value;
//   let result = "";

//   if (option === "1") {
//     const rooftopArea = parseFloat(document.getElementById("slider").value);
//     result = `You entered Total Rooftop Area: ${rooftopArea} sq ft`;
//   } else if (option === "2") {
//     const panelCapacity = parseFloat(document.getElementById("slider").value);
//     result = `You entered Solar Panel Capacity: ${panelCapacity} kW`;
//   } else if (option === "3") {
//     const budget = parseFloat(document.getElementById("slider").value);
//     result = `You entered Budget: $${budget}`;
//   } else if (option === "4") {
//     const electricityCost = parseFloat(document.getElementById("electricityCost").value);
//     result = `You entered Average Electricity Cost: ₹${electricityCost} per KWh`;
//   }

//   const category = document.getElementById("category").value;
//   result += `, Category: ${category}`;
//   document.getElementById("result").innerText = result;
// }

// document.getElementById("electricityCost").addEventListener("input", function() {
//   document.getElementById("electricityCostSlider").value = this.value;
// });

// document.getElementById("electricityCostSlider").addEventListener("input", function() {
//   document.getElementById("electricityCost").value = this.value;
// });


  
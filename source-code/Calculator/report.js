function calculateSolarPanelSize(budget, rooftopArea, monthlyElectricityConsumption, averageElectricityCost, ghi, systemEfficiency) {
    // Convert monthly electricity consumption to daily consumption
    const dailyElectricityConsumption = (monthlyElectricityConsumption * 12) / 365;
  
    // Calculate solar radiation per day
    const solarRadiationPerDay = ghi;
  
    // Calculate solar panel capacity required in kW
    const solarPanelCapacity = dailyElectricityConsumption / (solarRadiationPerDay * systemEfficiency);
  
    // Calculate total cost of electricity per year
    const annualElectricityCost = dailyElectricityConsumption * 365 * averageElectricityCost;
  
    // Calculate maximum affordable solar panel capacity based on budget
    const maxAffordableCapacity = (budget * rooftopArea) / solarPanelCapacity;
  
    return {
      solarPanelCapacity,
      annualElectricityCost,
      maxAffordableCapacity
    };
}

function calculateProposedBudget(solarPanelCapacity) {
    const standardRate = 55000; // Standard rate set by the Indian Government in Rs./kWh
    const proposedBudget = solarPanelCapacity * standardRate;
    return proposedBudget;
}

function calculateCostRecoveryTime(proposedBudget, averageElectricityCost, monthlyElectricityConsumption) {
    // Calculate annual savings from solar panel
    const annualSavings = monthlyElectricityConsumption * 12 * averageElectricityCost; // Assuming no increase in electricity cost
  
    // Calculate cost recovery time in years
    const costRecoveryTime = proposedBudget / annualSavings;
  
    return costRecoveryTime;
}

function calculateProposedBudgetPerFlat(solarPanelCapacity, numberOfFlats) {
    const standardRate = 55000; // Standard rate set by the Indian Government in Rs./kWh
    const totalProposedBudget = solarPanelCapacity * standardRate;
    const proposedBudgetPerFlat = totalProposedBudget / numberOfFlats;
    return proposedBudgetPerFlat;
}

// Add event listener to the Calculate button
document.getElementById('calculateBtn').addEventListener('click', function() {
    // Retrieve input values
    const budget = parseFloat(document.getElementById('budget').value);
    const rooftopArea = parseFloat(document.getElementById('roofarea').value);
    const monthlyElectricityConsumption = parseFloat(document.getElementById('unitsconsumed').value);
    const averageElectricityCost = parseFloat(document.getElementById('electricityCost').value);
    const category = document.getElementById('category').value;
    const numberOfFlats = category === 'apartment' ? parseFloat(document.getElementById('flats').value) : 1; // Default to 1 if not apartment

    const ghi = 5; // Example value
    const systemEfficiency = 0.75; // Example value

    // Calculate solar panel size
    const result = calculateSolarPanelSize(budget, rooftopArea, monthlyElectricityConsumption, averageElectricityCost, ghi, systemEfficiency);

    // Calculate proposed budget
    const proposedBudget = calculateProposedBudget(result.solarPanelCapacity);

    // Calculate cost recovery time
    const costRecoveryTime = calculateCostRecoveryTime(proposedBudget, averageElectricityCost, monthlyElectricityConsumption);

    // Calculate proposed budget per flat if category is apartment
    const proposedBudgetPerFlat = category === 'apartment' ? calculateProposedBudgetPerFlat(result.solarPanelCapacity, numberOfFlats) : 0;

    // Update HTML with results
    const resultElement = document.getElementById('result');
    resultElement.innerHTML = `
        <p>Solar Panel Capacity Required: ${result.solarPanelCapacity.toFixed(2)} kW</p>
        <p>Annual Electricity Cost: ₹${result.annualElectricityCost.toFixed(2)}</p>
        
        <p>Proposed Budget: ₹${proposedBudget.toFixed(2)}</p>
        <p>Cost Recovery Time: ${costRecoveryTime.toFixed(2)} years</p>
        <p>Proposed Budget per Flat: ₹${proposedBudgetPerFlat.toFixed(2)}</p>
    `;
});


  
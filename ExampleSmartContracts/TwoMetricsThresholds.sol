pragma solidity ^0.4.11;


contract owned {
    //This is an official solidity snippet from http://solidity.readthedocs.io/en/develop/contracts.html
    function owned() {owner = msg.sender;}

    address owner;
    // This contract only defines a modifier but does not use
    // it - it will be used in derived contracts.
    // The function body is inserted where the special symbol
    // This means that if the owner calls this function, the
    // function is executed and otherwise, an exception is
    // thrown.
    modifier onlyOwner {
        require(msg.sender == owner);
        _;
    }
}


contract example is owned {
    int16 constant PhysPropertyUnitOfMeasurementLT = - 42;

    int16 constant PhysPropertyUnitOfMeasurementUT = 42;

    int16 constant AnotherExampleLT = - 42;

    int16 constant AnotherExampleUT = 42;

    event AlarmPhysPropertyUnitOfMeasurement(int16 _valPhysPropertyUnitOfMeasurement, string _id);

    event AlarmAnotherExample(int16 _valAnotherExample, string _id);

    event AlarmAll(
    int16 _valPhysPropertyUnitOfMeasurement, int16 _valAnotherExample, string _id
    );
    //The values returned by this function have the same order as the values listed at the beginning of this Smart Contract
    function getTriggers() constant onlyOwner
    returns (
    int16 PhysPropertyUnitOfMeasurementLT, int16 PhysPropertyUnitOfMeasurementUT, int16 AnotherExampleLT, int16 AnotherExampleUT){
        return (- 42, 42, - 42, 42);}

    function updatePhysPropertyUnitOfMeasurement(int16 _valPhysPropertyUnitOfMeasurement, string _id) onlyOwner {if (PhysPropertyUnitOfMeasurementLT > _valPhysPropertyUnitOfMeasurement || PhysPropertyUnitOfMeasurementUT < _valPhysPropertyUnitOfMeasurement) {AlarmPhysPropertyUnitOfMeasurement(_valPhysPropertyUnitOfMeasurement, _id);}}

    function updateAnotherExample(int16 _valAnotherExample, string _id) onlyOwner {if (AnotherExampleLT > _valAnotherExample || AnotherExampleUT < _valAnotherExample) {AlarmAnotherExample(_valAnotherExample, _id);}}

    function updateAll(
    int16 _valPhysPropertyUnitOfMeasurement, int16 _valAnotherExample, string _id
    ) onlyOwner
    {
        if (
        (PhysPropertyUnitOfMeasurementLT > _valPhysPropertyUnitOfMeasurement || PhysPropertyUnitOfMeasurementUT < _valPhysPropertyUnitOfMeasurement) &&
        (AnotherExampleLT > _valAnotherExample || AnotherExampleUT < _valAnotherExample)
        ) {
            AlarmAll(_valPhysPropertyUnitOfMeasurement, _valAnotherExample, _id);
        }
        else {
            if (PhysPropertyUnitOfMeasurementLT > _valPhysPropertyUnitOfMeasurement || PhysPropertyUnitOfMeasurementUT < _valPhysPropertyUnitOfMeasurement) {AlarmPhysPropertyUnitOfMeasurement(_valPhysPropertyUnitOfMeasurement, _id);}
            if (AnotherExampleLT > _valAnotherExample || AnotherExampleUT < _valAnotherExample) {AlarmAnotherExample(_valAnotherExample, _id);}
        }
    }
}

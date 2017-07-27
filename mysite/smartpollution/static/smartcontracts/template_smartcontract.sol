pragma solidity ^0.4.11;
contract owned {
  //This is an official solidity snippet from
  //http://solidity.readthedocs.io/en/develop/contracts.html
    function owned() { owner = msg.sender; }
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
contract @ContractName@ is owned {
  Metric public metric = Metric(@MetricName@, 0);
  LowerTrigger lowerTrigger = LowerTrigger(@LowerTrigger@);
  UpperTrigger upperTrigger = UpperTrigger(@UpperTrigger@);
    struct Metric{
        string name;   // name of the metric
        int@Int@ value; // this value is the
    }
    struct LowerTrigger{
      int32 value;
    }
    struct UpperTrigger{
      int32 value;
    }
    event ValueChanged(
      int32 _value
    );
    event Alarm(
      string _alarm,
      int32 _value
    );
    function update(
      int32 _value
      ) onlyOwner
      {
        metric.value=_value;
        ValueChanged(_value);
        //if lower trigger is violated
        if(metric.value<lowerTrigger.value){
          Alarm('Lower trigger has been violated, Current value:', metric.value);
        }
        if(metric.value>upperTrigger.value){
          Alarm('Upper trigger has been violated, Current value:', metric.value);
        }
      }
      function changeLowerTrigger(
        int32 _value
        )onlyOwner{
          lowerTrigger.value=_value;
      }
      function changeUpperTrigger(
        int32 _value
        )onlyOwner{
          upperTrigger.value=_value;
      }
}

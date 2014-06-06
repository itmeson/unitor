Desmos Test
###########

:date: 2014-06-03
:tags: desmos, graphing, units
:category: nullresult


.. raw:: html

    <script src="https://www.desmos.com/api/v0.3/calculator.js?apiKey=dcb31709b452b1cf9dc26972add0fda6"></script>

    <div id="calculator" style="width: 100%; height: 600px;"></div>

    <script>
      var elt = document.getElementById('calculator');
      var calculator = Desmos.Calculator(elt, {menus: true});
      calculator.setViewport([0,1000,0,1000]);
      calculator.setExpressions([
	{id:'a-slider', latex:'a=2', max:50} ,
	{id:'graph1', latex:'y=ax'},
	{id:'x-val', latex:'x=10'}
      ]);
      
    </script>


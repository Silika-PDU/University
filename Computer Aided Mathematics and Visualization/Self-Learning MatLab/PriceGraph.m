prices = [42000; 40020; 41900; 42500; 43000; 62800; 53200; 44000; 43500; 44200]
windowSize = 2;
sma = movmean(prices, windowSize);
figure;
plot(prices, 'b-', 'LineWidth', 1.5); 
hold on;
plot(sma, 'r--', 'LineWidth', 2);   
legend('Raw Prices', '3-Period Moving Average', 'Location', 'NorthWest');
xlabel('Time Periods');
ylabel('Price ($)');
title('Basic Quantitative Moving Average');
grid on;
returns = diff(prices) ./ prices(1:end-1) * 100;
disp('Percentage Returns per period (%):');
disp(returns);
if prices(end) > sma(end)
    disp('Signal: BUY (Price is riding above the moving average)');
else
    disp('Signal: SELL (Price has dropped below the moving average)');
end

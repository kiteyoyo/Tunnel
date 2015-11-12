function O=sub(A,B)
O=[A(1,:) ; (A(2:end,:)-B(2:end,:))];
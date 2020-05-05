%sum of numbers of mulitples of 3 and 5 below 1000

-module(multiples_of_3_and_5).
 -export([sum/1, sum_multiples/1]).



sum_multiples(Number) ->
    V = fun(X) 
                when (X rem 3 == 0) or (X rem 5 == 0) -> X;
            (X)
               when (X rem 3 =/= 0) or (X rem 5 =/= 0) -> 0
        end,
       Z =  lists:map(V, Number),
        lists:sum(Z).

sum(L) -> sum(L, 0).

sum([], Sum) -> Sum;
sum([H |T], Sum) -> sum(T, H+Sum).


% sum(L) -> sum(L,0).
 
% sum([], Sum) -> Sum;
% sum([H|T], Sum) -> sum(T, H+Sum).
    % Target = Number -1,
    % Sum = 0,
    % case (Target rem 3 == 0) or (Target rem 5 == 0) of 
    %     true -> Sum + Target    
    % end.


%    Totals = fun(Value) when Target < Number ->
%         Sum = 0,
%          case Target rem 3 == 0 or (Target rem 5 == 0)  of 
%              true -> Sum + Target;
%             false -> io:format("isnot working boo")
%         end
%     end,
%     Totals.


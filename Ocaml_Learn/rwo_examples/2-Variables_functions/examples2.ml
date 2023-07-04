open Base
open Stdio
open Core_bench

(* time function *)
let time f x =
  let t = Unix.gettimeofday () in
  let fx = f x in
  printf "execution elapsed time: %F sec\n" (Unix.gettimeofday () -. t);
  fx

(* try to program fizzbuzz *)
let inp = 100

let fizzbuzz inList =
  let checkDiv num =
    if num % 15 = 0 then "fizzbuzz"
    else if num % 3 = 0 then "fizz"
    else if num % 5 = 0 then "buzz"
    else Int.to_string num
  in
  List.map inList ~f:(fun x -> checkDiv x)

let fizzbuzz_2 inList =
  let checkDiv_2 num =
    match (num % 3, num % 5) with
    | 0, 0 -> "fizzbuzz"
    | 0, _ -> "fizz"
    | _, 0 -> "buzz"
    | _, _ -> Int.to_string num
  in
  List.map inList ~f:(fun x -> checkDiv_2 x)
;;

fizzbuzz (List.range 1 inp);;
fizzbuzz_2 (List.range 1 inp)

(* Function to reverse a string using recursion*)
(* Atempt 1 - list manipulation *)
let revString str =
  let rec revList inList =
    match inList with [] -> [] | hd :: tail -> revList tail @ [ hd ]
  in
  String.of_list (revList (String.to_list str))

(* Not using recursion *)
let rev x =
  let len = String.length x in
  String.init len ~f:(fun n -> String.get x (len - n - 1))

(* Benchmark *)
let testStr = "Hello";;

printf "rec 1 result:%s\n" (revString testStr);
time revString testStr
;;

printf "Non-rec result:%s\n" (rev testStr);
time rev testStr

(* alternative Benchmark *)
(* [
     Bench.Test.create ~name:"Rev_Rec" (fun () -> revString testStr);
     Bench.Test.create ~name:"Rev_Non_Rec" (fun () -> rev testStr);
   ]
   |> Bench.bench *)
(* ------------------------------------------------------ *)


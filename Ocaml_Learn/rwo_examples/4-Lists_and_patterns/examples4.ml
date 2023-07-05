open Base
open Stdio
(* open Core_bench *)

let rec find_first_repeat list =
  match list with
  | [] | [ _ ] ->
      (* only zero or one elements, so no repeats *)
      None
  | x :: y :: tl -> if x = y then Some x else find_first_repeat (y :: tl)

(* The |> opetator can be used swap the placement of function and argument allowing to chain functions without naming each return *)
let path = "/usr/bin:/usr/local/bin:/bin:/sbin:/usr/bin";;

String.split ~on:':' path
|> List.dedup_and_sort ~compare:String.compare
|> List.iter ~f:print_endline

(* Function to rmove num from the array *)
let rec dropValue l to_drop =
  match l with
  | [] -> []
  | hd :: tl ->
      let newTail = dropValue tl to_drop in
      if hd = to_drop then newTail else hd :: newTail

let () = List.iter ~f:(printf "%d ") (dropValue [ 1; 2; 3; 3; 4; 3; 5; 9 ] 3)

(* Function render_table that, given a list of column headers and a list of rows, prints them out in a well-formatted text table. *)

let t_headers = [ "language"; "architect"; "first release" ]

let t_rows =
  [
    [ "Lisp"; "John McCarthy"; "1958" ];
    [ "C"; "Dennis Ritchie"; "1969" ];
    [ "ML"; "Robin Milner"; "1973" ];
    [ "OCaml"; "Xavier Leroy"; "1996" ];
  ]
(*
   | language | architect      | first release |
   |----------+----------------+---------------|
   | Lisp     | John McCarthy  | 1958          |
   | C        | Dennis Ritchie | 1969          |
   | ML       | Robin Milner   | 1973          |
   | OCaml    | Xavier Leroy   | 1996          |
*)

(* function to compute the maximum width of each column of data *)

let max_widths header rows =
  let lengths l = List.map ~f:String.length l in
  List.fold rows ~init:(lengths header) ~f:(fun acc row ->
      List.map2_exn ~f:Int.max acc (lengths row))

(* Create the line that separates the heder from the rows *)
(* Create strings of dashes based on the max size for the col *)

let widths = max_widths t_headers t_rows

let buildSep width =
  let n_dashes = List.map ~f:(fun l -> String.make l '-') width in
  "|-" ^ String.concat n_dashes ~sep:"-+-" ^ "-|"

let padStr txt_in desired_width =
  txt_in ^ String.make (desired_width - String.length txt_in) ' '

let render_row row widths_list =
  List.map2_exn row widths_list ~f:(fun item w -> "| " ^ padStr item w ^ " |")
;;

printf "seprator :%s \n" (buildSep widths)
(*
   let rec buildSep n_dash =
     let sep = "" in
     match n_dash with [] -> "" | hd :: tl -> sep ^ hd *)

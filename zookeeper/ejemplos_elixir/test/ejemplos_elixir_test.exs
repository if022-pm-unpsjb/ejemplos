defmodule EjemplosElixirTest do
  use ExUnit.Case
  doctest EjemplosElixir

  test "greets the world" do
    assert EjemplosElixir.hello() == :world
  end
end

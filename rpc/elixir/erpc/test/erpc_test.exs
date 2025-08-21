defmodule ErpcTest do
  use ExUnit.Case
  doctest Erpc

  test "greets the world" do
    assert Erpc.hello() == :world
  end
end

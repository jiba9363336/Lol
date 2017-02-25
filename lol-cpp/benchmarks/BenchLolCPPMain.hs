{-|
Module      : BenchLolCPPMain
Description : Main driver for Lol benchmarks with CPP.
Copyright   : (c) Eric Crockett, 2011-2017
                  Chris Peikert, 2011-2017
License     : GPL-2
Maintainer  : ecrockett0@email.com
Stability   : experimental
Portability : POSIX

Main driver for Lol benchmarks with CPP.
-}

{-# LANGUAGE DataKinds      #-}
{-# LANGUAGE NamedFieldPuns #-}
{-# LANGUAGE TypeOperators  #-}

module BenchLolCPPMain where

import Crypto.Lol.Benchmarks
import Crypto.Lol.Benchmarks.Standard
import Crypto.Lol.Cyclotomic.Tensor.CPP
import Crypto.Lol.Factored
import qualified Crypto.Lol.Utils.PrettyPrint.Diagnostic as D
import qualified Crypto.Lol.Utils.PrettyPrint.Table as T
import Crypto.Random.DRBG

import Data.Proxy

-- choose which layers of Lol to benchmark
ls :: [String]
ls = [
  "STensor",
  "Tensor",
  "SUCyc",
  "UCyc",
  "Cyc"
  ]

-- choose which operations to benchmark
bs :: [String]
bs = [
  "unzipPow",
  "unzipDec",
  "unzipCRT",
  "zipWith (*)",
  "crt",
  "crtInv",
  "l",
  "lInv",
  "*g Pow",
  "*g Dec",
  "*g CRT",
  "divg Pow",
  "divg Dec",
  "divg CRT",
  "lift",
  "error",
  "twacePow",
  "twaceDec",
  "twaceCRT",
  "embedPow",
  "embedDec",
  "embedCRT"
  ]

main :: IO ()
main = diagnosticMain

tableMain :: IO ()
tableMain = do
  let opts = (T.defaultOpts $ Just "UCyc"){T.benches=bs}
  g1 <- defaultBenches (Proxy::Proxy CT)
  mapM_ (T.prettyBenches opts) g1

diagnosticMain :: IO ()
diagnosticMain = do
  let opts = D.defaultOpts{D.levels=ls, D.benches=bs}
  b1 <- benchGroup "Single Index"
          [oneIdxBenches (Proxy::Proxy '(F64*F9*F25, Zq 14401)) (Proxy::Proxy CT) (Proxy::Proxy HashDRBG)]
  b2 <- benchGroup "Twace-Embed"
          [twoIdxBenches (Proxy::Proxy '(F64*F9*F25, F64*F9*F25, Zq 14401)) (Proxy::Proxy CT)]
  mapM_ (D.prettyBenches opts) [b1,b2]

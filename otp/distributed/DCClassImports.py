# This file was generated by the parse_dclass.py utility.
from pandac.PandaModules import *


hashVal = 877728986


from toontown.coghq import DistributedCashbotBossSafe, DistributedCashbotBossCrane, DistributedBattleFactory, DistributedCashbotBossTreasure, DistributedCogHQDoor, DistributedSellbotHQDoor, DistributedFactoryElevatorExt, DistributedMintElevatorExt, DistributedLawOfficeElevatorExt, DistributedLawOfficeElevatorInt, LobbyManager, DistributedMegaCorp, DistributedFactory, DistributedLawOffice, DistributedLawOfficeFloor, DistributedLift, DistributedDoorEntity, DistributedSwitch, DistributedButton, DistributedTrigger, DistributedCrushableEntity, DistributedCrusherEntity, DistributedStomper, DistributedStomperPair, DistributedLaserField, DistributedGolfGreenGame, DistributedSecurityCamera, DistributedMover, DistributedElevatorMarker, DistributedBarrelBase, DistributedGagBarrel, DistributedBeanBarrel, DistributedHealBarrel, DistributedGrid, ActiveCell, DirectionalCell, CrusherCell, DistributedCrate, DistributedSinkingPlatform, BattleBlocker, DistributedMint, DistributedMintRoom, DistributedMintBattle, DistributedStage, DistributedStageRoom, DistributedStageBattle, DistributedLawbotBossGavel, DistributedLawbotCannon, DistributedLawbotChair, DistributedCogKart, DistributedCountryClub, DistributedCountryClubRoom, DistributedMoleField, DistributedCountryClubBattle, DistributedMaze, DistributedFoodBelt, DistributedBanquetTable, DistributedGolfSpot
from toontown.golf import DistributedPhysicsWorld, DistributedGolfHole, DistributedGolfCourse
from toontown.building import DistributedAnimatedProp, DistributedTrophyMgr, DistributedBuilding, DistributedAnimBuilding, DistributedBuildingQueryMgr, DistributedToonInterior, DistributedToonHallInterior, DistributedSuitInterior, DistributedHQInterior, DistributedGagshopInterior, DistributedPetshopInterior, DistributedKartShopInterior, DistributedLibraryInterior, DistributedDoor, DistributedAnimDoor, DistributedKnockKnockDoor, DistributedElevator, DistributedElevatorFSM, DistributedElevatorExt, DistributedElevatorInt, DistributedElevatorFloor, DistributedBossElevator, DistributedVPElevator, DistributedCFOElevator, DistributedCJElevator, DistributedBBElevator, DistributedBoardingParty, DistributedTutorialInterior, DistributedClubElevator
from toontown.uberdog.DistributedPartyManager import DistributedPartyManager
from otp.friends import FriendManager, PlayerFriendsManager, GuildManager, FriendInfo, AvatarFriendInfo
from otp.level import DistributedLevel, DistributedEntity, DistributedInteractiveEntity
from toontown.shtiker import DeleteManager, PurchaseManager, NewbiePurchaseManager
from toontown.groups import GroupManager
from toontown.uberdog.ClientServicesManager import ClientServicesManager
from toontown.ai import WelcomeValleyManager, NewsManager, DistributedAprilToonsMgr, DistributedBlackCatMgr, DistributedReportMgr, DistributedPolarBearMgr, DistributedPolarPlaceEffectMgr, DistributedGreenToonEffectMgr, DistributedResistanceEmoteMgr, DistributedScavengerHuntTarget, DistributedTrickOrTreatTarget, DistributedWinterCarolingTarget, DistributedSillyMeterMgr
from otp.chat import ChatAgent
from toontown.parties.GlobalPartyManager import GlobalPartyManager
from toontown.racing.DistributedStartingBlock import DistributedViewingBlock
from toontown.pets.PetDCImports import *
from toontown.suit import DistributedSuitPlanner, DistributedSuitBase, DistributedSuit, DistributedTutorialSuit, DistributedFactorySuit, DistributedMintSuit, DistributedStageSuit, DistributedSellbotBoss, DistributedCashbotBoss, DistributedCashbotBossGoon, DistributedGoon, DistributedGridGoon, DistributedLawbotBoss, DistributedLawbotBossSuit, DistributedBossbotBoss
from toontown.distributed import ToontownDistrict, ToontownDistrictStats, DistributedTimer
from toontown.effects import DistributedFireworkShow
from toontown.safezone import DistributedTrolley, DistributedPartyGate, DistributedBoat, DistributedButterfly, DistributedMMPiano, DistributedDGFlower, DistributedFishingSpot, SafeZoneManager, DistributedTreasure, DistributedGolfKart, DistributedPicnicBasket, DistributedGameTable, DistributedChineseCheckers, DistributedCheckers, DistributedFindFour
from toontown.fishing import DistributedFishingPond, DistributedFishingTarget, DistributedPondBingoManager
from toontown.minigame import DistributedMinigame, DistributedMinigameTemplate, DistributedRaceGame, DistributedCannonGame, DistributedPhotoGame, DistributedPatternGame, DistributedRingGame, DistributedTagGame, DistributedMazeGame, DistributedTugOfWarGame, DistributedCatchGame, DistributedDivingGame, DistributedTargetGame, DistributedTravelGame, DistributedPairingGame, DistributedVineGame, DistributedIceGame, DistributedCogThiefGame, DistributedTwoDGame
from toontown.racing import DistributedVehicle, DistributedStartingBlock, DistributedRace, DistributedKartPad, DistributedRacePad, DistributedViewPad, DistributedStartingBlock, DistributedLeaderBoard, DistributedGag, DistributedProjectile
from toontown.catalog import CatalogManager, AccountDate
from toontown.rpc.AwardManager import AwardManager
from toontown.parties import DistributedParty, DistributedPartyActivity, DistributedPartyTeamActivity, DistributedPartyCannon, DistributedPartyCannonActivity, DistributedPartyCatchActivity, DistributedPartyWinterCatchActivity, DistributedPartyCogActivity, DistributedPartyWinterCogActivity, DistributedPartyFireworksActivity, DistributedPartyDanceActivityBase, DistributedPartyDanceActivity, DistributedPartyDance20Activity, DistributedPartyValentineDanceActivity, DistributedPartyValentineDance20Activity, DistributedPartyTrampolineActivity, DistributedPartyValentineTrampolineActivity, DistributedPartyVictoryTrampolineActivity, DistributedPartyWinterTrampolineActivity, DistributedPartyTugOfWarActivity, DistributedPartyJukeboxActivityBase, DistributedPartyJukeboxActivity, DistributedPartyJukebox40Activity, DistributedPartyValentineJukeboxActivity, DistributedPartyValentineJukebox40Activity
from toontown.friends.TrueFriendsMgr import TrueFriendsMgr
from toontown.coghq.InGameEditorDCImports import *
from toontown.friends import TTPlayerFriendsManager, TTUFriendsManager
from toontown.cogdominium import DistributedCogdoInterior, DistributedCogdoBattleBldg, DistributedCogdoElevatorExt, DistributedCogdoElevatorInt, DistributedCogdoBarrel, DistCogdoGame, DistCogdoLevelGame, DistCogdoBoardroomGame, DistCogdoCraneGame, DistCogdoMazeGame, DistCogdoFlyingGame, DistCogdoCrane, DistCogdoCraneMoneyBag, DistCogdoCraneCog
from otp.distributed import Account, DistributedDistrict, DistributedDirectory
from toontown.estate import DistributedCannon, DistributedTarget, EstateManager, DistributedEstate, DistributedHouse, DistributedHouseInterior, DistributedGarden, DistributedHouseDoor, DistributedMailbox, DistributedFurnitureManager, DistributedFurnitureItem, DistributedBank, DistributedCloset, DistributedTrunk, DistributedPhone, DistributedFireworksCannon, DistributedLawnDecor, DistributedGardenPlot, DistributedGardenBox, DistributedFlower, DistributedGagTree, DistributedStatuary, DistributedToonStatuary, DistributedChangingStatuary, DistributedAnimatedStatuary, DistributedPlantBase, DistributedLawnDecor
from toontown.toon import DistributedToon, DistributedNPCToonBase, DistributedNPCToon, DistributedSmartNPC, DistributedSmartNPC, DistributedNPCSpecialQuestGiver, DistributedNPCFlippyInToonHall, DistributedNPCScientist, DistributedNPCClerk, DistributedNPCTailor, DistributedNPCBlocker, DistributedNPCFisherman, DistributedNPCPartyPerson, DistributedNPCPetclerk, DistributedNPCKartClerk, DistributedNPCGlove
from toontown.tutorial import DistributedBattleTutorial, TutorialManager
from toontown.pets import DistributedPetProxy
from toontown.coderedemption.TTCodeRedemptionMgr import TTCodeRedemptionMgr
from direct.distributed import DistributedObject, DistributedNode, DistributedSmoothNode, DistributedCartesianGrid, DistributedCamera, DistributedObjectGlobal
from otp.ai import TimeManager, MagicWordManager
from otp.avatar import DistributedAvatar, DistributedPlayer, AvatarHandle
from toontown.battle import DistributedBattleBase, DistributedBattle, DistributedBattleBldg, DistributedBattleFinal, DistributedBattleWaiters, DistributedBattleDiners


dcImports = locals().copy()

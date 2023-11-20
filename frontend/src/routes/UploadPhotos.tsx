import {
  Box,
  Button,
  Container,
  FormControl,
  Heading,
  Input,
  useToast,
  VStack,
} from "@chakra-ui/react";
import { useMutation } from "@tanstack/react-query";
import { useForm } from "react-hook-form";
import { useParams } from "react-router-dom";
import { createPhoto, getUploadURL, uploadImage } from "../api";
import useHostOnlyPage from "../components/HostOnlyPage";
import ProtectedPage from "../components/ProtectedPage";

interface IForm {
  file: FileList;
}

interface IForm {
  file: FileList;
}

interface IUploadURLResponse {
  id: string;
  uploadURL: string;
}

export default function UploadPhotos() {
  const { register, handleSubmit, watch, reset } = useForm<IForm>();
  const { roomId } = useParams();
  const toast = useToast();

  const createPhotoMutation = useMutation(createPhoto, {
    onSuccess: () => {
      toast({
        status: "success",
        title: "Image uploaded",
        isClosable: true,
        description: "Feel free to upload more images",
      });
      reset();
    },
  });

  const UploadImageMutation = useMutation(uploadImage, {
    onSuccess: ({result}: any) => {
        if (roomId) {
            createPhotoMutation.mutate({
            description: "I love react",
            file: `https://imagedelivery.net/aSbksvJjax-AUC7qVnaC4A/${result.id}/public`,
            roomId,
            });
        }
    },
  });

  const UploadURLMutation = useMutation(getUploadURL, {
        onSuccess: (data: IUploadURLResponse) => {
            UploadImageMutation.mutate({
                uploadURL: data.uploadURL,
                file: watch("file")
            })
        },
    });

  useHostOnlyPage();

  const onSubmit = (data: any) => {
    UploadURLMutation.mutate();
  };

  console.log(watch());
  return (
    <ProtectedPage>
      <Box
        pb={40}
        mt={10}
        px={{
          base: 10,
          lg: 40,
        }}
      >
        <Container>
          <Heading textAlign={"center"}>Upload a Photo</Heading>
          <VStack
            as="form"
            onSubmit={handleSubmit(onSubmit)}
            spacing={5}
            mt={10}
          >
            <FormControl>
              <Input {...register("file")} type="file" accept="image/*" />
            </FormControl>
            <Button
              isLoading={
                createPhotoMutation.isLoading ||
                UploadImageMutation.isLoading ||
                UploadURLMutation.isLoading
              }
              type="submit"
              w="full"
              colorScheme={"red"}
            >
              Upload photos
            </Button>
          </VStack>
        </Container>
      </Box>
    </ProtectedPage>
  );
}
